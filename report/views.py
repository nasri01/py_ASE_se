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
modellist = ['monitor_spo2', 'monitor_ecg', 'monitor_nibp', 'monitor_safety', 'defibrilator', 'aed', 'ecg',
             'infusion_pump', 'syringe_pump', 'spo2', 'flowmeter', 'anesthesia_machine', 'ventilator', 
              'suction', 'electrocauter', 'monometer','cant_test' ]

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
                for tc in obj.totalcomment.all():
                    tcomment.append(tc)
                row.append(obj.deivce.hospital.city.state_name.name)#0
                row.append(obj.deivce.hospital.city.name)#1
                row.append(obj.deivce.hospital.name)#2
                row.append(obj.deivce.section.name)#3
                row.append(obj.deivce.name.type.name)#4
                row.append(obj.deivce.name.creator.name)#5
                row.append(obj.deivce.name.name)#6
                row.append(obj.deivce.serial_number)#7
                row.append(obj.deivce.property_number)#8
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
        ss = 0
        sss = 0
        data = []
        for model in model_list:
            modelobj = model.objects.filter(licence__number=1003)
            if len(modelobj) == 1:
                if(model == monitor_spo2_1):
                    template_name = 'report/Monitor/Spo2/licence1.html'            
                    data.append((int(modelobj[0].s2_e1_spo2) - 70)**2)
                    data.append((int(modelobj[0].s2_e2_spo2) - 75)**2)
                    data.append((int(modelobj[0].s2_e3_spo2) - 80)**2)
                    data.append((int(modelobj[0].s2_e4_spo2) - 85)**2)
                    data.append((int(modelobj[0].s2_e5_spo2) - 88)**2)
                    data.append((int(modelobj[0].s2_e6_spo2) - 90)**2)
                    data.append((int(modelobj[0].s2_e7_spo2) - 92)**2)
                    data.append((int(modelobj[0].s2_e8_spo2) - 94)**2)
                    data.append((int(modelobj[0].s2_e9_spo2) - 96)**2)
                    data.append((int(modelobj[0].s2_e10_spo2) - 98)**2)
                    data.append((int(modelobj[0].s2_e11_spo2) - 100)**2)
                    for i in range(11):
                        ss+=data[i]
                    data.append(int(((ss/11)**0.5)*100)/100)

                    data.append((int(modelobj[0].s3_e1_pr) - 35)**2)
                    data.append((int(modelobj[0].s3_e2_pr) - 60)**2)
                    data.append((int(modelobj[0].s3_e3_pr) - 100)**2)
                    data.append((int(modelobj[0].s3_e4_pr) - 200)**2)
                    data.append((int(modelobj[0].s3_e5_pr) - 240)**2)
                    for i in range(12,17):
                        sss+=data[i]
                    data.append(int(((sss/5)**0.5)*100)/100)
                
                elif (model == monitor_nibp_1):
                    template_name = 'report/Monitor/NIBP/licence1.html'
                    data1=[]
                    data2=[]
                    data1.append(int(modelobj[0].s2_e1_pr1.split('/')[0]))##
                    data1.append(int(modelobj[0].s2_e1_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e1_pr3.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e2_pr1.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e2_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e2_pr3.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e3_pr1.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e3_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e3_pr3.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e4_pr1.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e4_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e4_pr3.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e5_pr1.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e5_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e5_pr3.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e6_pr1.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e6_pr2.split('/')[0]))
                    data1.append(int(modelobj[0].s2_e6_pr3.split('/')[0]))
                    data2.append(int(modelobj[0].s2_e1_pr1.split('/')[1]))##
                    data2.append(int(modelobj[0].s2_e1_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e1_pr3.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e2_pr1.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e2_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e2_pr3.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e3_pr1.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e3_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e3_pr3.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e4_pr1.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e4_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e4_pr3.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e5_pr1.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e5_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e5_pr3.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e6_pr1.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e6_pr2.split('/')[1]))
                    data2.append(int(modelobj[0].s2_e6_pr3.split('/')[1]))
                    data.append(sum(data1))
                    data.append(sum(data2))
                    data.append(round(np.mean(data1),2))
                    data.append(round(np.mean(data2),2))
                    data.append(round(np.std(data1),2))
                    data.append(round(np.std(data2),2))

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
                
                elif (model == suction_1):
                    template_name = 'report/suction/licence1.html'
                
                elif (model == syringe_pump_1):
                    template_name = 'report/syringe_pump/licence1.html'
                
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
            for model in model_list[:-2
            ]:
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
        ss = 0
        sss = 0
        data = []
        ddd = ' '#######
        for model in model_list:
            dd = model.objects.all()
            if len(dd) != 0:   
                for obj in dd :    
                    if(model == monitor_spo2_1):
                        template_name = 'report/Monitor/Spo2/licence1.html'            
                        data.append((int(obj.s2_e1_spo2) - 70)**2)
                        data.append((int(obj.s2_e2_spo2) - 75)**2)
                        data.append((int(obj.s2_e3_spo2) - 80)**2)
                        data.append((int(obj.s2_e4_spo2) - 85)**2)
                        data.append((int(obj.s2_e5_spo2) - 88)**2)
                        data.append((int(obj.s2_e6_spo2) - 90)**2)
                        data.append((int(obj.s2_e7_spo2) - 92)**2)
                        data.append((int(obj.s2_e8_spo2) - 94)**2)
                        data.append((int(obj.s2_e9_spo2) - 96)**2)
                        data.append((int(obj.s2_e10_spo2) - 98)**2)
                        data.append((int(obj.s2_e11_spo2) - 100)**2)
                        for i in range(11):
                            ss+=data[i]
                        data.append(int(((ss/11)**0.5)*100)/100)

                        data.append((int(obj.s3_e1_pr) - 35)**2)
                        data.append((int(obj.s3_e2_pr) - 60)**2)
                        data.append((int(obj.s3_e3_pr) - 100)**2)
                        data.append((int(obj.s3_e4_pr) - 200)**2)
                        data.append((int(obj.s3_e5_pr) - 240)**2)
                        for i in range(12,17):
                            sss+=data[i]
                        data.append(int(((sss/5)**0.5)*100)/100)
                    
                    elif (model == monitor_nibp_1):
                        template_name = 'report/Monitor/NIBP/licence1.html'
                        data1=[]
                        data2=[]
                        data1.append(int(obj.s2_e1_pr1.split('/')[0]))##
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
                        data2.append(int(obj.s2_e1_pr1.split('/')[1]))##
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
                        data.append(sum(data1))
                        data.append(sum(data2))
                        data.append(round(np.mean(data1),2))
                        data.append(round(np.mean(data2),2))
                        data.append(round(np.std(data1),2))
                        data.append(round(np.std(data2),2))

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
                    
                    elif (model == suction_1):
                        template_name = 'report/suction/licence1.html'
                    
                    elif (model == syringe_pump_1):
                        template_name = 'report/syringe_pump/licence1.html'
                    
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
                   
                    if not os.path.exists(f'{obj.request.number}/'):
                        os.makedirs(f'{obj.request.number}/')
                   
                    HTML(string=html).write_pdf(f'{obj.request.number}/{obj.licence.number}.pdf',font_config=font_config, stylesheets=[css1, css2])
                    
                    
                    a12 = report.objects.create(tt = ad_test_type0.objects.get(type=modellist[s]),device = obj.device,
                                            request = obj.request, date = obj.date, user = obj.user, status = obj.status,
                                            record = rd.objects.create(number=int(rd.objects.last().number)+1),
                                            licence = lcc.objects.create(number=int(lcc.objects.last().number)+1),
                                             is_done = obj.is_done)
                    
                    for w in obj.totalcomment.all():
                        if(model == monitor_spo2_1):
                            a12.monitor_spo2_totalcomment.add(w)
                        
                        elif (model == monitor_nibp_1):
                            a12.monitor_nibp_totalcomment.add(w)

                        elif (model == monitor_ecg_1):
                            a12.monitor_ecg_totalcomment.add(w)

                        elif (model == monitor_safety_1):
                            a12.monitor_safety_totalcomment.add(w)

                        elif (model == aed_1):
                            a12.aed_totalcomment.add(w)

                        elif (model == anesthesia_machine_1):
                            a12.anesthesia_machine_totalcomment.add(w)

                        elif (model == defibrilator_1):
                            a12.defibrilator_totalcomment.add(w)
                        
                        elif (model == ecg_1):
                            a12.ecg_totalcomment.add(w)
                        
                        elif (model == electrocauter_1):
                            a12.electrocauter_totalcomment.add(w)
                        
                        elif (model == flowmeter_1):
                            a12.flowmeter_totalcomment.add(w)
                        
                        elif (model == infusion_pump_1):
                            a12.infusion_pump_totalcomment.add(w)
                        
                        elif (model == monometer_1):
                            a12.monometer_totalcomment.add(w)
                        
                        elif (model == spo2_1):
                            a12.spo2_totalcomment.add(w)
                        
                        elif (model == suction_1):
                            a12.suction_totalcomment.add(w)
                        
                        elif (model == syringe_pump_1):
                            a12.syringe_pump_totalcomment.add(w)
                        
                        elif (model == ventilator_1):
                            a12.ventilator_totalcomment.add(w)
                    a12.save()
                    obj.delete()
            s+=1
        return HttpResponse('done :)')
    else: 
        raise Http404
