import io, pytz, xlsxwriter, jdatetime, os
from jdatetime import timedelta
import numpy as np
from form.models import *
from .models import report

from .models import record as rd
from .models import licence as lcc
from acc.models import ad_excel_arg, aUserProfile, Request, device_type, ad_test_type0

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render ,Http404
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import weasyprint

model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, defibrilator_1, aed_1, ecg_1,
                infusion_pump_1, syringe_pump_1, spo2_1, flowmeter_1, anesthesia_machine_1, ventilator_1, 
                suction_1, electrocauter_1, monometer_1, cant_test ,report ]
                #TODO organize
modellist = ['monitor_spo2', 'monitor ECG', 'monitor NIBP', 'monitor Safety', 'Defibrilator', 'AED', 'ECG',
             'Infusion Pump', 'Syringe Pump', 'Pulse Oximetry', 'Flow Meter', 'Anesthesia Machine', 'Ventilator', 
              'Suction', 'ElectroCouter', 'Mano Meter','cant_test' ]

def xlsx(request):
    if request.method == 'GET':
        
        ey, em, ed = request.GET['end_date'].split('/')
        sy, sm, sd = request.GET['start_date'].split('/')
        ey = int(ey)
        em = int(em)
        ed = int(ed)
        sy = int(sy)
        sm = int(sm)
        sd = int(sd)
        new_start_date = jdatetime.date(sy, sm, sd) - timedelta(days=1)
        # because quering from data base we should consider filter data via utc time
        start = jdatetime.datetime(new_start_date.year, new_start_date.month, new_start_date.day, 19, 30).astimezone(
            pytz.timezone('UTC'))
        end = jdatetime.datetime(ey, em, ed, 19, 30).astimezone(pytz.timezone('UTC'))
        if end < start:
            return render(request, 'acc/hospital/index.html', {'date_error': 'بازه زمانی وارد شده نا معتبر است',
                                                               'flag': 1})  # , 'date': jdatetime.date.today(),
            # 'month': mm

        ##Create Excel
        tcomment = []
        row = []
        data = []
        data1 = []
        try:
            if request.GET['is_recal'] == 'on':
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id).filter(is_recal=True)
                    data1.append(modelobj)       
                    
        except:
            for model in model_list:
                modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                    request__hospital__user__id__exact=request.user.id)
                data1.append(modelobj)

        for obj1 in data1:
            for obj in obj1:
                tcomment = []
                row = []
                try:
                    for tc in obj.totalcomment.all():
                        tcomment.append(tc)
                except:
                    for ml in modellist:
                        if obj.tt == ml:
                            pass
                row.append(obj.device.hospital.city.state_name.name)#0
                row.append(obj.device.hospital.city.name)#1
                row.append(obj.device.hospital.name)#2
                row.append(obj.device.section.name)#3
                row.append(obj.device.name.type.name)#4
                row.append(obj.device.name.creator.name)#5
                row.append(obj.device.name.name)#6
                row.append(obj.device.serial_number)#7
                row.append(obj.device.property_number)#8
                row.append(obj.status.status)#9
                row.append(obj.date.strftime("%Y-%m-%d"))#10
                if obj.licence.number != -1 :
                    row.append(obj.licence.number)#11
                else:
                    row.append('-')#11
                row.append(tcomment)#12*
                data.append(row)    


        fr1 = ad_excel_arg.objects.all().order_by('order')
        if request.GET['action'] == 'download':

            output = io.BytesIO()
            wb = xlsxwriter.Workbook(output)
            ws = wb.add_worksheet()
            ws.right_to_left()
            ws.set_default_row(height=40)
            ws.set_column(0, 15, 17)

            ##first row
            first_row = (str(fr1[1]),
                         str(fr1[2]),
                         str(fr1[3]),
                         str(fr1[4]),
                         str(fr1[5]),
                         str(fr1[6]),
                         str(fr1[7]),
                         str(fr1[8]),
                         str(fr1[9]),
                         str(fr1[10]),
                         str(fr1[11]),
                         str(fr1[12]),
                         str(fr1[13]),
                         str(fr1[14]),
                         str(fr1[15])
                         )
            fr = wb.add_format({'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'bottom': True, 'left': True})

            ws.write_row(row=0, col=0, data=first_row, cell_format=fr)
            # Patterns
            gg = wb.add_format(  # accept
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'green',
                 'bottom': True,
                 'left': True})
            yy = wb.add_format(  # conditional
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'yellow',
                 'bottom': True,
                 'left': True})
            rr = wb.add_format(  # reject
                {'font_size': 11, 'align': 'center', 'valign': 'vcenter', 'pattern': 1, 'bg_color': 'red',
                 'bottom': True,
                 'left': True})
            cursor = 1

            for idata in data:
                # if (modelobj[i].device.hospital.user == request.user):
                # Assign Status
                if idata.status.id == 1:  # accept
                    fstate = gg
                elif idata.status.id == 2:  # conditional
                    fstate = yy
                elif idata.status.id == 3:  # conditional
                    fstate = rr
                else:
                    fstate = fr
                total_com = ''
                for t in idata[12]:
                    total_com += f'{t}-'

                data = (cursor,
                        idata[0],
                        idata[1],
                        idata[2],
                        idata[3],
                        idata[4],
                        idata[5],
                        idata[6],
                        idata[7],
                        idata[8],
                        idata[9],
                        idata[10],
                        str(fr1[0]),
                        idata[11],
                        total_com,
                        )

                ws.write_row(row=cursor, col=0, data=data, cell_format=fstate)
                cursor += 1
            wb.close()

            output.seek(0)
            filename = f'Azma_Saba.ExcelReport.{str(jdatetime.date.today()).split()[0]}.xlsx'
            response = HttpResponse(output,
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=%s' % filename

            return response


        else:  # display table
            auser = aUserProfile.objects.get(user=request.user)
            req = Request.objects.filter(hospital__user=request.user).order_by('date')
            for t in req:
                t.date = t.date.today()
            return render(request, 'acc/hospital/index.html',
                          {'firstrow': fr1, 'data': data,'request': req,'auser': auser })
                            # 'date':jdatetime.date.today(),'month': mm

    # return render(request, 'acc/hospital/index.html', { 'status': 'Successfully Created!','hflag':1})
    # return FileResponse(wb,as_attachment=True,filename=f'report {datetime.date.today()}.xlsx')


# def pdf(request):
#     t = monitor_spo2_1.objects.get(pk=1)
#     t2 = jdatetime.datetime.today()

#     return render(request, 'report/Monitor/Spo2/licence1/cover.html', {'spo2': t, 'day': t2})


def pdf1(request):
    if request.method == 'GET':
        
        data = []
        for model in model_list:
            modelobj = model.objects.filter(licence__number=1003)
            if len(modelobj) == 1:
                if(model == monitor_spo2_1):
                    template_name = 'report/Monitor/Spo2/licence1.html'            
                    ss = 0
                    sss = 0            
                    data.append((int(modelobj[0].s2_e1_spo2) - 70)**2)#0
                    data.append((int(modelobj[0].s2_e2_spo2) - 75)**2)#1
                    data.append((int(modelobj[0].s2_e3_spo2) - 80)**2)#2
                    data.append((int(modelobj[0].s2_e4_spo2) - 85)**2)#3
                    data.append((int(modelobj[0].s2_e5_spo2) - 88)**2)#4
                    data.append((int(modelobj[0].s2_e6_spo2) - 90)**2)#5
                    data.append((int(modelobj[0].s2_e7_spo2) - 92)**2)#6
                    data.append((int(modelobj[0].s2_e8_spo2) - 94)**2)#7
                    data.append((int(modelobj[0].s2_e9_spo2) - 96)**2)#8
                    data.append((int(modelobj[0].s2_e10_spo2) - 98)**2)#9
                    data.append((int(modelobj[0].s2_e11_spo2) - 100)**2)#10
                    for i in range(11):
                        ss+=data[i]
                    data.append(int(((ss/11)**0.5)*100)/100)#11

                    data.append((int(modelobj[0].s3_e1_pr) - 35)**2)#12
                    data.append((int(modelobj[0].s3_e2_pr) - 60)**2)#13
                    data.append((int(modelobj[0].s3_e3_pr) - 100)**2)#14
                    data.append((int(modelobj[0].s3_e4_pr) - 200)**2)#15
                    data.append((int(modelobj[0].s3_e5_pr) - 240)**2)#16
                    for i in range(12,17):
                        sss+=data[i]
                    data.append(int(((sss/5)**0.5)*100)/100)#17
                
                elif (model == monitor_nibp_1):
                    template_name = 'report/Monitor/NIBP/licence1.html'
                    data1 = []
                    data2 = []
                    data3 = []
                    data1.append(int(modelobj[0].s2_e1_pr1.split('/')[0]))#14
                    data1.append(int(modelobj[0].s2_e1_pr2.split('/')[0]))#15
                    data1.append(int(modelobj[0].s2_e1_pr3.split('/')[0]))#16
                    data1.append(int(modelobj[0].s2_e2_pr1.split('/')[0]))#17
                    data1.append(int(modelobj[0].s2_e2_pr2.split('/')[0]))#18
                    data1.append(int(modelobj[0].s2_e2_pr3.split('/')[0]))#19
                    data1.append(int(modelobj[0].s2_e3_pr1.split('/')[0]))#20
                    data1.append(int(modelobj[0].s2_e3_pr2.split('/')[0]))#21
                    data1.append(int(modelobj[0].s2_e3_pr3.split('/')[0]))#22
                    data1.append(int(modelobj[0].s2_e4_pr1.split('/')[0]))#23
                    data1.append(int(modelobj[0].s2_e4_pr2.split('/')[0]))#24
                    data1.append(int(modelobj[0].s2_e4_pr3.split('/')[0]))#25
                    data1.append(int(modelobj[0].s2_e5_pr1.split('/')[0]))#26
                    data1.append(int(modelobj[0].s2_e5_pr2.split('/')[0]))#27
                    data1.append(int(modelobj[0].s2_e5_pr3.split('/')[0]))#28
                    data1.append(int(modelobj[0].s2_e6_pr1.split('/')[0]))#29
                    data1.append(int(modelobj[0].s2_e6_pr2.split('/')[0]))#30
                    data1.append(int(modelobj[0].s2_e6_pr3.split('/')[0]))#31
                    data2.append(int(modelobj[0].s2_e1_pr1.split('/')[1]))#32
                    data2.append(int(modelobj[0].s2_e1_pr2.split('/')[1]))#33
                    data2.append(int(modelobj[0].s2_e1_pr3.split('/')[1]))#34
                    data2.append(int(modelobj[0].s2_e2_pr1.split('/')[1]))#35
                    data2.append(int(modelobj[0].s2_e2_pr2.split('/')[1]))#36
                    data2.append(int(modelobj[0].s2_e2_pr3.split('/')[1]))#37
                    data2.append(int(modelobj[0].s2_e3_pr1.split('/')[1]))#38
                    data2.append(int(modelobj[0].s2_e3_pr2.split('/')[1]))#39
                    data2.append(int(modelobj[0].s2_e3_pr3.split('/')[1]))#40
                    data2.append(int(modelobj[0].s2_e4_pr1.split('/')[1]))#41
                    data2.append(int(modelobj[0].s2_e4_pr2.split('/')[1]))#42
                    data2.append(int(modelobj[0].s2_e4_pr3.split('/')[1]))#43
                    data2.append(int(modelobj[0].s2_e5_pr1.split('/')[1]))#44
                    data2.append(int(modelobj[0].s2_e5_pr2.split('/')[1]))#45
                    data2.append(int(modelobj[0].s2_e5_pr3.split('/')[1]))#46
                    data2.append(int(modelobj[0].s2_e6_pr1.split('/')[1]))#47
                    data2.append(int(modelobj[0].s2_e6_pr2.split('/')[1]))#48
                    data2.append(int(modelobj[0].s2_e6_pr3.split('/')[1]))#49
                    if (abs(int(modelobj[0].s1_e1_simp) - int(modelobj[0].s1_e1_nibpp)) >= 3):#6
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e2_simp) - int(modelobj[0].s1_e2_nibpp)) >= 3):#7
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e3_simp) - int(modelobj[0].s1_e3_nibpp)) >= 3.6):#8
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e4_simp) - int(modelobj[0].s1_e4_nibpp)) >= 6):#9
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e5_simp) - int(modelobj[0].s1_e5_nibpp)) >= 3):#10
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e6_simp) - int(modelobj[0].s1_e6_nibpp)) >= 3):#11
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e7_simp) - int(modelobj[0].s1_e7_nibpp)) >= 3.6):#12
                        data3.append(0)
                    else:
                        data3.append(1)
                    if (abs(int(modelobj[0].s1_e8_simp) - int(modelobj[0].s1_e8_nibpp)) >= 6):#13
                        data3.append(0)
                    else:
                        data3.append(1)
                    
                    
                    
                    data.append(sum(data1))#0
                    data.append(sum(data2))#1
                    data.append(round(np.mean(data1),2))#2
                    data.append(round(np.mean(data2),2))#3
                    data.append(round(np.std(data1),2))#4
                    data.append(round(np.std(data2),2))#5
                    
                    data.append(data3)#6
                    data.append(data1)#7
                    data.append(data2)#8

                elif (model == monitor_ecg_1):
                    template_name = 'report/Monitor/ECG/licence1.html'

                elif (model == monitor_safety_1):
                    template_name = 'report/Monitor/SAFETY/licence1.html'

                elif (model == aed_1):
                    template_name = 'report/aed/licence1.html'

                elif (model == anesthesia_machine_1):
                    template_name = 'report/anesthesiamachine/licence1.html'

                elif (model == defibrilator_1):
                    template_name = 'report/defibrilator/licence1.html'
                
                elif (model == ecg_1):
                    template_name = 'report/ecg/licence1.html'
                
                elif (model == electrocauter_1):
                    template_name = 'report/electrocauter/licence1.html'
                
                elif (model == flowmeter_1):
                    template_name = 'report/flowmeter/licence1.html'
                
                elif (model == infusion_pump_1):
                    template_name = 'report/infusion_pump/licence1.html'
                
                elif (model == monometer_1):
                    template_name = 'report/monometer/licence1.html'
                
                elif (model == spo2_1):
                    template_name = 'report/spo2/licence1.html'
                    ss = 0
                    sss = 0            
                    data.append((int(modelobj[0].s2_e1_spo2) - 70)**2)#0
                    data.append((int(modelobj[0].s2_e2_spo2) - 75)**2)#1
                    data.append((int(modelobj[0].s2_e3_spo2) - 80)**2)#2
                    data.append((int(modelobj[0].s2_e4_spo2) - 85)**2)#3
                    data.append((int(modelobj[0].s2_e5_spo2) - 88)**2)#4
                    data.append((int(modelobj[0].s2_e6_spo2) - 90)**2)#5
                    data.append((int(modelobj[0].s2_e7_spo2) - 92)**2)#6
                    data.append((int(modelobj[0].s2_e8_spo2) - 94)**2)#7
                    data.append((int(modelobj[0].s2_e9_spo2) - 96)**2)#8
                    data.append((int(modelobj[0].s2_e10_spo2) - 98)**2)#9
                    data.append((int(modelobj[0].s2_e11_spo2) - 100)**2)#10
                    for i in range(11):
                        ss+=data[i]
                    data.append(int(((ss/11)**0.5)*100)/100)#11

                    data.append((int(modelobj[0].s3_e1_pr) - 35)**2)#12
                    data.append((int(modelobj[0].s3_e2_pr) - 60)**2)#13
                    data.append((int(modelobj[0].s3_e3_pr) - 100)**2)#14
                    data.append((int(modelobj[0].s3_e4_pr) - 200)**2)#15
                    data.append((int(modelobj[0].s3_e5_pr) - 240)**2)#16
                    for i in range(12,17):
                        sss+=data[i]
                    data.append(int(((sss/5)**0.5)*100)/100)#17
                
                elif (model == suction_1):
                    template_name = 'report/suction/licence1.html'
                    data.append(abs(int(modelobj[0].s1_e1_rr)))#0
                    data.append(abs(int(modelobj[0].s1_e2_rr)))#1
                    data.append(abs(int(modelobj[0].s1_e3_rr) - 100))#2
                    data.append(abs(int(modelobj[0].s1_e4_rr) - 0.1))#3
                    data.append(abs(int(modelobj[0].s1_e5_rr) - 200))#4
                    data.append(abs(int(modelobj[0].s1_e6_rr - 0.3)))#5
                    data.append(abs(int(modelobj[0].s1_e7_rr) - 400))#6
                    data.append(abs(int(modelobj[0].s1_e8_rr) - 0.5))#7
                    data.append(abs(int(modelobj[0].s1_e9_rr) - 500))#8
                    data.append(abs(int(modelobj[0].s1_e10_rr) - 0.7))#9
                    data.append(abs(int(modelobj[0].s2_e1_rr)))#10/////
                    data.append(abs(int(modelobj[0].s2_e2_rr)))#11
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 38))#12
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 50))#13
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 76))#14
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 100))#15
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 114))#16
                    data.append(abs(int(modelobj[0].s2_e2_rr) - 150))#17


                elif (model == syringe_pump_1):
                    template_name = 'report/syringe_pump/licence1.html'
                    data.append(abs((int(modelobj[0].s6_e1_mf) - 50)*2))#0
                    data.append(abs(int(modelobj[0].s6_e1_mf) - 100))#1
                
                elif (model == ventilator_1):
                    template_name = 'report/ventilator/licence1.html'

                break

            # TODO licence doesn't exist
        usr= aUserProfile.objects.get(user=modelobj[0].user)
        t2 = jdatetime.datetime.today()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = (
            'inline; '
            f'filename=licence.pdf'
        )

        font_config = FontConfiguration()
        
        html = render_to_string(template_name, {
            'form': modelobj[0], 'time': t2,'usr':usr,'data':data
        })

        css_root = static('/css')
        css1 = CSS(filename=f'ww/{css_root}/sop2-pdf.css')
        css2 = CSS(filename=f'ww/{css_root}/bootstrap-v4.min.css')

        document = HTML(string=html).write_pdf(response,font_config=font_config, stylesheets=[css1, css2])

        return response

def req_summary(request):
    if request.method == 'GET':
        if request.GET['request'] == '1':#get sections
            sections = []
            for model in model_list:
                temp = model.objects.filter(request__number__exact=int(request.GET['req_number']))
                if len(temp) != 0:
                    for t in temp:
                        sections.append(t.device.section)
            sections = list(set(sections)) #get unique values 
            for sec in sections:
                sec = sec.name
        
            return render(request,'acc/employee/dlsum.html',{'data':sections,'req_num':request.GET['req_number']})
        
        elif request.GET['request'] == '0':#get report
            s = 0
            data = []
            sn = request.GET['sec_name']
            rn = int(request.GET['req_num'])
            types = device_type.objects.get(id__gte=13)
            for model in model_list[:-2]:
                temp = model.objects.filter(request__number__exact = rn).filter(#number of test of each device
                    device__section__name__exact = sn)
                temp2 = cant_test.objects.filter(request__number__exact=rn).filter(#number of cant test of each device
                    device__section__name__exact= sn ).filter(tt__type__exact=ad_test_type0.objects.all().order_by('id')[s/2])
                data[s] = len(temp)
                data[s+1] = len(temp2)     
                s += 2
            
            t2 = jdatetime.datetime.today()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = (
                'inline; '
                f'filename=summary_{sn}_{rn}.pdf'
            )
            font_config = FontConfiguration()
            #TODO add hospital infos
            html = render_to_string('report/sections_summary.html', {
                'time': t2,'data':data
            })

            css_root = static('/css')
            css1 = CSS(filename=f'ww/{css_root}/sop2-pdf.css')
            css2 = CSS(filename=f'ww/{css_root}/bootstrap-v4.min.css')

            document = HTML(string=html).write_pdf(response,font_config=font_config, stylesheets=[css1, css2])

            return response
                

def pdf(request):
    if request.method == 'GET':
        s = 0
        
        for model in model_list[:-2]:
            dd = model.objects.all()
            if len(dd) != 0:   
                for obj in dd : 
                    data = []   
                    if(model == monitor_spo2_1):
                        template_name = 'report/Monitor/Spo2/licence1.html'            
                        ss = 0
                        sss = 0            
                        data.append((int(obj.s2_e1_spo2) - 70)**2)#0
                        data.append((int(obj.s2_e2_spo2) - 75)**2)#1
                        data.append((int(obj.s2_e3_spo2) - 80)**2)#2
                        data.append((int(obj.s2_e4_spo2) - 85)**2)#3
                        data.append((int(obj.s2_e5_spo2) - 88)**2)#4
                        data.append((int(obj.s2_e6_spo2) - 90)**2)#5
                        data.append((int(obj.s2_e7_spo2) - 92)**2)#6
                        data.append((int(obj.s2_e8_spo2) - 94)**2)#7
                        data.append((int(obj.s2_e9_spo2) - 96)**2)#8
                        data.append((int(obj.s2_e10_spo2) - 98)**2)#9
                        data.append((int(obj.s2_e11_spo2) - 100)**2)#10
                        for i in range(11):
                            ss+=data[i]
                        data.append(int(((ss/11)**0.5)*100)/100)#11

                        data.append((int(obj.s3_e1_pr) - 35)**2)#12
                        data.append((int(obj.s3_e2_pr) - 60)**2)#13
                        data.append((int(obj.s3_e3_pr) - 100)**2)#14
                        data.append((int(obj.s3_e4_pr) - 200)**2)#15
                        data.append((int(obj.s3_e5_pr) - 240)**2)#16
                        for i in range(12,17):
                            sss+=data[i]
                        data.append(int(((sss/5)**0.5)*100)/100)#17
                    
                    elif (model == monitor_nibp_1):
                        template_name = 'report/Monitor/NIBP/licence1.html'
                        data1 = []
                        data2 = []
                        data3 = []
                        
                        data3.append(abs(int(obj.s1_e1_simp) - int(obj.s1_e1_nibpp)))   
                        data3.append(abs(int(obj.s1_e2_simp) - int(obj.s1_e2_nibpp)))                       
                        data3.append(abs(int(obj.s1_e3_simp) - int(obj.s1_e3_nibpp)))                       
                        data3.append(abs(int(obj.s1_e4_simp) - int(obj.s1_e4_nibpp)))                       
                        data3.append(abs(int(obj.s1_e5_simp) - int(obj.s1_e5_nibpp)))                        
                        data3.append(abs(int(obj.s1_e6_simp) - int(obj.s1_e6_nibpp)))                       
                        data3.append(abs(int(obj.s1_e7_simp) - int(obj.s1_e7_nibpp)))                       
                        data3.append(abs(int(obj.s1_e8_simp) - int(obj.s1_e8_nibpp)))                       
                             
                        data1.append(int(obj.s2_e1_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e1_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e1_pr3.split('/')[0]))
                        data1.append(int(obj.s2_e2_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e2_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e2_pr3.split('/')[0]))
                        data1.append(int(obj.s2_e3_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e3_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e3_pr3.split('/')[0]))
                        data1.append(int(obj.s2_e4_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e4_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e4_pr3.split('/')[0]))
                        data1.append(int(obj.s2_e5_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e5_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e5_pr3.split('/')[0]))
                        data1.append(int(obj.s2_e6_pr1.split('/')[0]))
                        data1.append(int(obj.s2_e6_pr2.split('/')[0]))
                        data1.append(int(obj.s2_e6_pr3.split('/')[0]))
                        data2.append(int(obj.s2_e1_pr1.split('/')[1]))#####
                        data2.append(int(obj.s2_e1_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e1_pr3.split('/')[1]))
                        data2.append(int(obj.s2_e2_pr1.split('/')[1]))
                        data2.append(int(obj.s2_e2_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e2_pr3.split('/')[1]))
                        data2.append(int(obj.s2_e3_pr1.split('/')[1]))
                        data2.append(int(obj.s2_e3_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e3_pr3.split('/')[1]))
                        data2.append(int(obj.s2_e4_pr1.split('/')[1]))
                        data2.append(int(obj.s2_e4_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e4_pr3.split('/')[1]))
                        data2.append(int(obj.s2_e5_pr1.split('/')[1]))
                        data2.append(int(obj.s2_e5_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e5_pr3.split('/')[1]))
                        data2.append(int(obj.s2_e6_pr1.split('/')[1]))
                        data2.append(int(obj.s2_e6_pr2.split('/')[1]))
                        data2.append(int(obj.s2_e6_pr3.split('/')[1]))
                        
                        
                        data.append(sum(data1))#0
                        data.append(sum(data2))#1
                        data.append(round(np.mean(data1),2))#2
                        data.append(round(np.mean(data2),2))#3
                        data.append(round(np.std(data1),2))#4
                        data.append(round(np.std(data2),2))#5
                        data.append(data3)#6
                        
                        for id in range(3):
                            data1[id] = abs(data1[id] - 30)
                            data2[id] = abs(data2[id] - 60)
                        for id in range(3,6):
                            data1[id] = abs(data1[id] - 50)
                            data2[id] = abs(data2[id] - 80)
                        for id in range(6,9):
                            data1[id] = abs(data1[id] - 80)
                            data2[id] = abs(data2[id] - 120)
                        for id in range(9,12):
                            data1[id] = abs(data1[id] - 150)
                            data2[id] = abs(data2[id] - 200)
                        for id in range(12,15):
                            data1[id] = abs(data1[id] - 15)
                            data2[id] = abs(data2[id] - 35)
                        for id in range(15,18):
                            data1[id] = abs(data1[id] - 70)
                            data2[id] = abs(data2[id] - 100)
                        data.append(data1)#7
                        data.append(data2)#8

                    elif (model == monitor_ecg_1):
                        template_name = 'report/Monitor/ECG/licence1.html'

                    elif (model == monitor_safety_1):
                        template_name = 'report/Monitor/SAFETY/licence1.html'

                    elif (model == aed_1):
                        template_name = 'report/aed/licence1.html'

                    elif (model == anesthesia_machine_1):
                        template_name = 'report/anesthesiamachine/licence1.html'

                    elif (model == defibrilator_1):
                        template_name = 'report/defibrilator/licence1.html'
                    
                    elif (model == ecg_1):
                        template_name = 'report/ecg/licence1.html'
                    
                    elif (model == electrocauter_1):
                        template_name = 'report/electrocauter/licence1.html'
                        data.append(abs(obj.s3a_e1_m - obj.s3a_e1_s))#0
                        data.append((abs(obj.s3a_e1_m - obj.s3a_e1_m) / obj.s3a_e1_s) * 100)#1
                        data.append(abs(obj.s3a_e2_m - obj.s3a_e2_s))#2
                        data.append((abs(obj.s3a_e2_m - obj.s3a_e2_s) / obj.s3a_e2_s) * 100)#3
                        data.append(abs(obj.s3a_e3_m - obj.s3a_e3_s))#4
                        data.append((abs(obj.s3a_e3_m - obj.s3a_e3_s) / obj.s3a_e3_s) * 100)#5
                        data.append(abs(obj.s3b_e1_m - obj.s3b_e1_s))#6
                        data.append((abs(obj.s3b_e1_m - obj.s3b_e1_s) / obj.s3b_e1_s) * 100)#7
                        data.append(abs(obj.s3b_e2_m - obj.s3b_e2_s))#8
                        data.append((abs(obj.s3b_e2_m - obj.s3b_e2_s) / obj.s3b_e2_s) * 100)#9
                        data.append(abs(obj.s3b_e3_m - obj.s3b_e3_s))#10
                        data.append((abs(obj.s3b_e3_m - obj.s3b_e3_s) / obj.s3b_e3_s) * 100)#11
                        data.append(abs(obj.s3c_e1_m - obj.s3c_e1_s))#12
                        data.append((abs(obj.s3c_e1_m - obj.s3c_e1_s) / obj.s3c_e1_s) * 100)#13
                        data.append(abs(obj.s3c_e2_m - obj.s3c_e2_s))#14
                        data.append((abs(obj.s3c_e2_m - obj.s3c_e2_s) / obj.s3c_e2_s) * 100)#15
                        data.append(abs(obj.s3c_e3_m - obj.s3c_e3_s))#16
                        data.append((abs(obj.s3c_e3_m - obj.s3c_e3_s) / obj.s3c_e3_s) * 100)#17
                        data.append(abs(obj.s3d_e1_m - obj.s3d_e1_s))#18
                        data.append((abs(obj.s3d_e1_m - obj.s3d_e1_s) / obj.s3d_e1_s) * 100)#19
                        data.append(abs(obj.s3d_e2_m - obj.s3d_e2_s))#20
                        data.append((abs(obj.s3d_e2_m - obj.s3d_e2_s) / obj.s3d_e2_s) * 100)#21
                        data.append(abs(obj.s3d_e3_m - obj.s3d_e3_s))#22
                        data.append((abs(obj.s3d_e3_m - obj.s3d_e3_s) / obj.s3d_e3_s) * 100)#23
                        data.append(abs(obj.s3e_e1_m - obj.s3e_e1_s))#24
                        data.append((abs(obj.s3e_e1_m - obj.s3e_e1_s) / obj.s3e_e1_s) * 100)#25
                        data.append(abs(obj.s3e_e2_m - obj.s3e_e2_s))#26
                        data.append((abs(obj.s3e_e2_m - obj.s3e_e2_s) / obj.s3e_e2_s) * 100)#27
                        data.append(abs(obj.s3e_e3_m - obj.s3e_e3_s))#28
                        data.append((abs(obj.s3e_e3_m - obj.s3e_e3_s) / obj.s3e_e3_s) * 100)#29





                    
                    elif (model == flowmeter_1):
                        template_name = 'report/flowmeter/licence1.html'
                        data.append(abs(int(obj.s1_e1_rlpm) - 0.5))#0
                        data.append(abs(int(obj.s1_e2_rlpm) - 2))#1
                        data.append(abs(int(obj.s1_e3_rlpm) - 4))#2
                        data.append(abs(int(obj.s1_e4_rlpm) - 7))#3
                        data.append(abs(int(obj.s1_e5_rlpm) - 10))#4
                        data.append(abs(int(obj.s1_e6_rlpm) - 15))#5
                        data.append(data[0] * 200)#6
                        data.append(data[1] * 50)#7
                        data.append(data[2] * 25)#8
                        data.append(round(data[3] * (100/7), 2))#9
                        data.append(data[4] * 10)#10
                        data.append(round(data[5] * (100/15), 2))#11

                    elif (model == infusion_pump_1):
                        template_name = 'report/infusion_pump/licence1.html'
                        data.append(abs((int(obj.s6_e1_mf) - 50)*2))#0
                        data.append(abs(int(obj.s6_e1_mf) - 100))#1
                    
                    elif (model == monometer_1):
                        template_name = 'report/monometer/licence1.html'
                    
                    elif (model == spo2_1):
                        template_name = 'report/spo2/licence1.html'
                        ss = 0
                        sss = 0            
                        data.append((int(obj.s2_e1_spo2) - 70)**2)#0
                        data.append((int(obj.s2_e2_spo2) - 75)**2)#1
                        data.append((int(obj.s2_e3_spo2) - 80)**2)#2
                        data.append((int(obj.s2_e4_spo2) - 85)**2)#3
                        data.append((int(obj.s2_e5_spo2) - 88)**2)#4
                        data.append((int(obj.s2_e6_spo2) - 90)**2)#5
                        data.append((int(obj.s2_e7_spo2) - 92)**2)#6
                        data.append((int(obj.s2_e8_spo2) - 94)**2)#7
                        data.append((int(obj.s2_e9_spo2) - 96)**2)#8
                        data.append((int(obj.s2_e10_spo2) - 98)**2)#9
                        data.append((int(obj.s2_e11_spo2) - 100)**2)#10
                        for i in range(11):
                            ss+=data[i]
                        data.append(int(((ss/11)**0.5)*100)/100)#11

                        data.append((int(obj.s3_e1_pr) - 35)**2)#12
                        data.append((int(obj.s3_e2_pr) - 60)**2)#13
                        data.append((int(obj.s3_e3_pr) - 100)**2)#14
                        data.append((int(obj.s3_e4_pr) - 200)**2)#15
                        data.append((int(obj.s3_e5_pr) - 240)**2)#16
                        for i in range(12,17):
                            sss+=data[i]
                        data.append(int(((sss/5)**0.5)*100)/100)#17
                    
                    elif (model == suction_1):
                        template_name = 'report/suction/licence1.html'
                        data.append(abs(int(obj.s1_e1_rr)))#0
                        data.append(abs(int(obj.s1_e2_rr)))#1
                        data.append(abs(int(obj.s1_e3_rr) - 100))#2
                        data.append(abs(int(obj.s1_e4_rr) - 0.1))#3
                        data.append(abs(int(obj.s1_e5_rr) - 200))#4
                        data.append(abs(int(obj.s1_e6_rr - 0.3)))#5
                        data.append(abs(int(obj.s1_e7_rr) - 400))#6
                        data.append(abs(int(obj.s1_e8_rr) - 0.5))#7
                        data.append(abs(int(obj.s1_e9_rr) - 500))#8
                        data.append(abs(int(obj.s1_e10_rr) - 0.7))#9
                        data.append(abs(int(obj.s2_e1_rr)))#10/////
                        data.append(abs(int(obj.s2_e2_rr)))#11
                        data.append(abs(int(obj.s2_e2_rr) - 38))#12
                        data.append(abs(int(obj.s2_e2_rr) - 50))#13
                        data.append(abs(int(obj.s2_e2_rr) - 76))#14
                        data.append(abs(int(obj.s2_e2_rr) - 100))#15
                        data.append(abs(int(obj.s2_e2_rr) - 114))#16
                        data.append(abs(int(obj.s2_e2_rr) - 150))#17


                    elif (model == syringe_pump_1):
                        template_name = 'report/syringe_pump/licence1.html'
                        data.append(abs((int(obj.s6_e1_mf) - 50)*2))#0
                        data.append(abs(int(obj.s6_e1_mf) - 100))#1
                    
                    elif (model == ventilator_1):
                        template_name = 'report/ventilator/licence1.html'


                    usr= aUserProfile.objects.get(user=obj.user)
                    t2 = jdatetime.datetime.today()
                    font_config = FontConfiguration()
                    html = render_to_string(template_name, {
                        'form': obj, 'time': t2,'usr':usr,'data':data })

                    
                    css_root = static('/css')
                    css1 = CSS(filename=f'ww/{css_root}/sop2-pdf.css')
                    css2 = CSS(filename=f'ww/{css_root}/bootstrap-v4.min.css')
                    if not os.path.exists('_reports/'):
                        os.makedirs('_reports/')
                    
                    if not os.path.exists(f'_reports/{obj.request.number}/'):
                        os.makedirs(f'_reports/{obj.request.number}/')
                        
                    HTML(string=html).write_pdf(f'_reports/{obj.request.number}/{obj.licence.number}.pdf',font_config=font_config, stylesheets=[css1, css2])
                    
                    
                    a12 = report.objects.create(tt = ad_test_type0.objects.get(type=modellist[s]),device = obj.device,
                                            request = obj.request, date = obj.date, user = obj.user, status = obj.status,
                                            record = rd.objects.create(number=int(rd.objects.last().number)+1),
                                            licence = lcc.objects.create(number=int(lcc.objects.last().number)+1),
                                             is_done = obj.is_done, totalcomment = obj.totalcomment)
                    a12.save()
                    # obj.delete()
            s+=1
        return HttpResponse('done :)')
    else: 
        raise Http404
