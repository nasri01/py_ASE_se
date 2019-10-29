import io, pytz, xlsxwriter, jdatetime
from jdatetime import timedelta
import numpy as np
from form.models import *
from acc.models import ad_excel_arg, aUserProfile, Request, device_type, ad_test_type0

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, defibrilator_1, aed_1, ecg_1,
                infusion_pump_1, syringe_pump_1, spo2_1, flowmeter_1, anesthesia_machine_1, ventilator_1, 
                suction_1, electrocauter_1, monometer_1, 
                ]


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
            # if (jdatetime.date.today().month < 10):
            #     mm = f'0{jdatetime.date.today().month}'
            # else:
            #     mm = jdatetime.date.today().month
            return render(request, 'acc/hospital/index.html', {'date_error': 'بازه زمانی وارد شده نا معتبر است',
                                                               'flag': 1})  # , 'date': jdatetime.date.today(),
            # 'month': mm

        ##Create Excel
        data = []
        try:
            if request.GET['is_recal'] == 'on':
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id).filter(is_recal=True)
                    data.extend(modelobj)
        except:
            for model in model_list:
                modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                    request__hospital__user__id__exact=request.user.id)
                data.extend(modelobj)

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
                for t in idata.totalcomment.all():
                    total_com += f'{t}-'

                data = (cursor,
                        idata.device.hospital.city.state_name.name,
                        idata.device.hospital.city.name,
                        idata.device.hospital.name,
                        idata.device.section.name,
                        idata.device.name.type.name,
                        idata.device.name.creator.name,
                        idata.device.name.name,
                        idata.device.serial_number,
                        idata.device.property_number,
                        idata.status.status,
                        str(idata.date.astimezone(pytz.timezone('Asia/Tehran'))).split()[0],
                        str(fr1[0]),
                        idata.licence.number,
                        total_com
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
        try:#get sections
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
        except:#get report
            s = 0
            data = []
            sn = request.GET['sec_name']
            rn = int(request.GET['req_num'])
            types = device_type.objects.get(id__gte=13)
            for model in model_list:
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
                
