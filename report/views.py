import io
import pytz
import xlsxwriter
import jdatetime
import os
import hashlib
from statistics import mean, stdev
from ftplib import FTP
from jdatetime import timedelta
from form.models import *
from acc.models import licence as acc_licence
from .models import report, encode
from ww.local_settings import dl_ftp_host, dl_ftp_passwd, dl_ftp_user, dl_domain_name, domain_name


from acc.models import ad_excel_arg, aUserProfile, Request, device_type, ad_test_type0

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User, Group
from django.shortcuts import render, Http404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import weasyprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, defibrilator_1, aed_1, ecg_1,
              infusion_pump_1, syringe_pump_1, spo2_1, flowmeter_1, anesthesia_machine_1, ventilator_1,
              suction_1, electrocauter_1, monometer_1, cant_test, report]
modellist = ['monitor Spo2', 'monitor ECG', 'monitor NIBP', 'monitor Safety', 'Defibrilator', 'AED', 'ECG',
             'Infusion Pump', 'Syringe Pump', 'Pulse Oximetry', 'Flow Meter', 'Anesthesia Machine', 'Ventilator',
             'Suction', 'ElectroCauter', 'Mano Meter', 'cant_test']


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
        end = jdatetime.datetime(
            ey, em, ed, 19, 30).astimezone(pytz.timezone('UTC'))
        if end < start:
            return render(request, 'acc/hospital/index.html', {'date_error': 'بازه زمانی وارد شده نا معتبر است',
                                                               'flag': 1})  # , 'date': jdatetime.date.today(),
            # 'month': mm

        # Create Excel
        row = []
        data = []
        data1 = []
        try:
            if request.GET['is_recal'] == 'on':
                recal = True
        except:
            recal = False

        if recal:
            if Group.objects.get(name='admin') in request.user.groups.all():  # admin
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(
                        date__lte=end).filter(is_recal=True)
                    data1.append(modelobj)
            else:  # hospital
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id).filter(is_recal=True)
                    data1.append(modelobj)
        else:
            if Group.objects.get(name='admin') in request.user.groups.all():
                for model in model_list:
                    modelobj = model.objects.filter(
                        date__gte=start).filter(date__lte=end)
                    data1.append(modelobj)
            else:  # Hospital
                for model in model_list:
                    modelobj = model.objects.filter(
                        date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id)
                    data1.append(modelobj)

        for iii, obj1 in enumerate(data1):
            for obj in obj1:
                row = []
                row.append(obj.device.hospital.city.state_name.name)  # 0
                row.append(obj.device.hospital.city.name)  # 1
                row.append(obj.device.hospital.name)  # 2
                row.append(obj.device.section.name)  # 3
                row.append(obj.device.name.type.name)  # 4
                row.append(obj.device.name.creator.name)  # 5
                row.append(obj.device.name.name)  # 6
                row.append(obj.device.serial_number)  # 7
                if str(obj.device.property_number) != 'None':
                    row.append(obj.device.property_number)  # 8
                else:
                    row.append('-')
                row.append(obj.status.status)  # 9
                row.append(obj.date.strftime("%Y-%m-%d"))  # 10
                if obj.status.id != 4:
                    row.append(obj.licence.number)  # 11
                else:
                    row.append('-')  # 11
                if iii == 0:
                    row.append('-SPO2-' + obj.totalcomment)  # 12*
                elif iii == 1:
                    row.append('-ECG-' + obj.totalcomment)  # 12*
                elif iii == 2:
                    row.append('-NIBP-' + obj.totalcomment)  # 12*
                elif iii == 3:
                    row.append('-Safety-' + obj.totalcomment)  # 12*
                else:
                    row.append(obj.totalcomment)  # 12*
                row.append(obj.status.id)  # 13
                data.append(row)
        print(data)
        fr1 = ad_excel_arg.objects.all().order_by('id')
        if request.GET['action'] == 'download':

            output = io.BytesIO()
            wb = xlsxwriter.Workbook(output)
            ws = wb.add_worksheet()
            ws.right_to_left()
            ws.set_default_row(height=40)
            ws.set_column(0, 15, 17)

            # first row
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
                         str(fr1[15]),
                         'PDF'
                         )
            fr = wb.add_format({'font_size': 11, 'align': 'center',
                                'valign': 'vcenter', 'bottom': True, 'left': True})

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
                if idata[13] == 1:  # accept
                    fstate = gg
                elif idata[13] == 2:  # conditional
                    fstate = yy
                elif idata[13] == 3:  # conditional
                    fstate = rr
                else:
                    fstate = fr

                data = (cursor,
                        idata[0],  # ostan
                        idata[1],  # shahr
                        idata[2],  # name moshtari
                        idata[3],  # mahale esteqrar
                        idata[4],  # mahsul
                        idata[5],  # tolid konande
                        idata[6],  # model
                        idata[7],  # shoamre serial
                        idata[8],  # kode amval
                        idata[9],  # vaziate azmoon
                        idata[10],  # tarikh calibration
                        str(fr1[0]),  # etebare calibration
                        idata[11],  # shomare govahi
                        idata[12],  # tozihat
                        )

                ws.write_row(row=cursor, col=0, data=data, cell_format=fstate)
                data1 = report.objects.filter(licence__number=idata[11])
                try:
                    name = encode.objects.get(hospital=data1[0].device.hospital)
                    ul = 'https://{}/{}/{}/{}/{}.pdf'.format(
                        dl_domain_name ,name.name, data1[0].request.number, data1[0].tt, data1[0].licence.number)
                    ws.write_url(row=cursor, col=len(data), url=ul,
                             cell_format=fstate, string='show', tip='Downlaod PDF')
                except:
                    pass
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

            chart = [0, 0, 0, 0]
            if request.user.groups.all()[0] == Group.objects.get(name='hospital'):
                req = Request.objects.filter(
                    hospital__user=request.user).order_by('date')
                template_name = 'acc/hospital/index.html'
            else:
                req = Request.objects.all().order_by('date')
                template_name = 'acc/admin/index.html'
            for obj1 in data1:
                chart[0] += len(obj1.filter(status__id=1))
                chart[1] += len(obj1.filter(status__id=2))
                chart[2] += len(obj1.filter(status__id=3))
                chart[3] += len(obj1.filter(status__id=4))

            for t in req:
                t.date = t.date.today()

            sent_data = {'firstrow': fr1, 'data': data,
                         'request': req, 'auser': auser, 'chart': chart}

            if request.user.groups.all()[0] == Group.objects.get(name='admin'):
                sent_data['admin'] = 1

            return render(request, template_name,
                          sent_data)
            # 'date':jdatetime.date.today(),'month': mm

    # return render(request, 'acc/hospital/index.html', { 'status': 'Successfully Created!','hflag':1})
    # return FileResponse(wb,as_attachment=True,filename=f'report {datetime.date.today()}.xlsx')


def req_summary(request):

    if request.method == 'GET':
        if request.GET['request'] == '1':  # get sections
            sections = []
            for model in model_list:
                temp = model.objects.filter(
                    request__number__exact=int(request.GET['req_number']))
                if len(temp) != 0:
                    for t in temp:
                        sections.append(t.device.section)
            sections = list(set(sections))  # get unique values
            for sec in sections:
                sec = sec.name

            return render(request, 'acc/employee/dlsum.html', {'data': sections, 'req_num': request.GET['req_number']})

        elif request.GET['request'] == '0':  # get report
            s = 0
            data = []
            sn = request.GET['sec_name']
            rn = int(request.GET['req_num'])
            types = device_type.objects.get(id__gte=13)
            for model in model_list[:-2]:
                temp = model.objects.filter(request__number__exact=rn).filter(  # number of test of each device
                    device__section__name__exact=sn)
                temp2 = cant_test.objects.filter(request__number__exact=rn).filter(  # number of cant test of each device
                    device__section__name__exact=sn).filter(tt__type__exact=ad_test_type0.objects.all().order_by('id')[s/2])
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
            # TODO add hospital infos
            html = render_to_string('report/sections_summary.html', {
                'time': t2, 'data': data
            })

            css_root = static('/css')
            css1 = CSS(filename=f'ww/{css_root}/sop2-pdf.css')
            css2 = CSS(filename=f'ww/{css_root}/bootstrap-v4.min.css')

            document = HTML(string=html).write_pdf(
                response, font_config=font_config, stylesheets=[css1, css2])

            return response


def send_file_ftp(ftp, filename):
    fp = open('report.pdf', 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(filename), fp, 1024)


def pdf(request):
    if request.method == 'GET':
        file = open('pdf_report.txt', 'at+')
        encode_file = open('encode.txt', 'at+')
        with FTP(
            host=dl_ftp_host,
            user=dl_ftp_user,
            passwd=dl_ftp_passwd
        ) as ftp:
            ftp.set_debuglevel(2)
            s = 0
            for model in model_list[:-2]:
                dd = model.objects.all()
                if len(dd) != 0:
                    for obj in dd:
    #===================================Begin-File Backing=================================================
                        data = []
                        if(model == monitor_spo2_1):
                            template_name = 'report/Monitor/Spo2/licence1.html'
                            ss = 0
                            sss = 0
                            data.append((int(obj.s2_e1_spo2) - 70)**2)  # 0
                            data.append((int(obj.s2_e2_spo2) - 75)**2)  # 1
                            data.append((int(obj.s2_e3_spo2) - 80)**2)  # 2
                            data.append((int(obj.s2_e4_spo2) - 85)**2)  # 3
                            data.append((int(obj.s2_e5_spo2) - 88)**2)  # 4
                            data.append((int(obj.s2_e6_spo2) - 90)**2)  # 5
                            data.append((int(obj.s2_e7_spo2) - 92)**2)  # 6
                            data.append((int(obj.s2_e8_spo2) - 94)**2)  # 7
                            data.append((int(obj.s2_e9_spo2) - 96)**2)  # 8
                            data.append((int(obj.s2_e10_spo2) - 98)**2)  # 9
                            data.append((int(obj.s2_e11_spo2) - 100)**2)  # 10
                            for i in range(11):
                                ss += data[i]
                            data.append(int(((ss/11)**0.5)*100)/100)  # 11

                            data.append((int(obj.s3_e1_pr) - 35)**2)  # 12
                            data.append((int(obj.s3_e2_pr) - 60)**2)  # 13
                            data.append((int(obj.s3_e3_pr) - 100)**2)  # 14
                            data.append((int(obj.s3_e4_pr) - 200)**2)  # 15
                            data.append((int(obj.s3_e5_pr) - 240)**2)  # 16
                            for i in range(12, 17):
                                sss += data[i]
                            data.append(int(((sss/5)**0.5)*100)/100)  # 17

                        elif (model == monitor_nibp_1):
                            template_name = 'report/Monitor/NIBP/licence1.html'
                            data1 = []
                            data2 = []
                            data3 = []

                            data3.append(
                                abs(int(obj.s1_e1_simp) - int(obj.s1_e1_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e2_simp) - int(obj.s1_e2_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e3_simp) - int(obj.s1_e3_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e4_simp) - int(obj.s1_e4_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e5_simp) - int(obj.s1_e5_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e6_simp) - int(obj.s1_e6_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e7_simp) - int(obj.s1_e7_nibpp)))
                            data3.append(
                                abs(int(obj.s1_e8_simp) - int(obj.s1_e8_nibpp)))

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
                            data2.append(int(obj.s2_e1_pr1.split('/')[1]))
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

                            for id in range(3):
                                data1[id] = abs(data1[id] - 30)
                                data2[id] = abs(data2[id] - 60)
                            for id in range(3, 6):
                                data1[id] = abs(data1[id] - 50)
                                data2[id] = abs(data2[id] - 80)
                            for id in range(6, 9):
                                data1[id] = abs(data1[id] - 80)
                                data2[id] = abs(data2[id] - 120)
                            for id in range(9, 12):
                                data1[id] = abs(data1[id] - 150)
                                data2[id] = abs(data2[id] - 200)
                            for id in range(12, 15):
                                data1[id] = abs(data1[id] - 15)
                                data2[id] = abs(data2[id] - 35)
                            for id in range(15, 18):
                                data1[id] = abs(data1[id] - 70)
                                data2[id] = abs(data2[id] - 100)

                            print(data1)
                            print(data2)
                            data.append(sum(data1))  # 0
                            data.append(sum(data2))  # 1
                            data.append(round(mean(data1), 2))  # 2
                            data.append(round(mean(data2), 2))  # 3
                            data.append(round(stdev(data1), 2))  # 4
                            data.append(round(stdev(data2), 2))  # 5
                            data.append(data3)  # 6

                            data.append(data1)  # 7
                            data.append(data2)  # 8

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
                            data.append(abs(obj.s3a_e1_m - obj.s3a_e1_s))  # 0
                            data.append(
                                (abs(obj.s3a_e1_m - obj.s3a_e1_m) / obj.s3a_e1_s) * 100)  # 1
                            data.append(abs(obj.s3a_e2_m - obj.s3a_e2_s))  # 2
                            data.append(
                                (abs(obj.s3a_e2_m - obj.s3a_e2_s) / obj.s3a_e2_s) * 100)  # 3
                            data.append(abs(obj.s3a_e3_m - obj.s3a_e3_s))  # 4
                            data.append(
                                (abs(obj.s3a_e3_m - obj.s3a_e3_s) / obj.s3a_e3_s) * 100)  # 5

                            data.append(abs(obj.s3b_e1_m - obj.s3b_e1_s))  # 6
                            data.append(
                                (abs(obj.s3b_e1_m - obj.s3b_e1_s) / obj.s3b_e1_s) * 100)  # 7
                            data.append(abs(obj.s3b_e2_m - obj.s3b_e2_s))  # 8
                            data.append(
                                (abs(obj.s3b_e2_m - obj.s3b_e2_s) / obj.s3b_e2_s) * 100)  # 9
                            data.append(abs(obj.s3b_e3_m - obj.s3b_e3_s))  # 10
                            data.append(
                                (abs(obj.s3b_e3_m - obj.s3b_e3_s) / obj.s3b_e3_s) * 100)  # 11

                            data.append(abs(obj.s3c_e1_m - obj.s3c_e1_s))  # 12
                            data.append(
                                (abs(obj.s3c_e1_m - obj.s3c_e1_s) / obj.s3c_e1_s) * 100)  # 13
                            data.append(abs(obj.s3c_e2_m - obj.s3c_e2_s))  # 14
                            data.append(
                                (abs(obj.s3c_e2_m - obj.s3c_e2_s) / obj.s3c_e2_s) * 100)  # 15
                            data.append(abs(obj.s3c_e3_m - obj.s3c_e3_s))  # 16
                            data.append(
                                (abs(obj.s3c_e3_m - obj.s3c_e3_s) / obj.s3c_e3_s) * 100)  # 17

                            data.append(abs(obj.s3d_e1_m - obj.s3d_e1_s))  # 18
                            data.append(
                                (abs(obj.s3d_e1_m - obj.s3d_e1_s) / obj.s3d_e1_s) * 100)  # 19
                            data.append(abs(obj.s3d_e2_m - obj.s3d_e2_s))  # 20
                            data.append(
                                (abs(obj.s3d_e2_m - obj.s3d_e2_s) / obj.s3d_e2_s) * 100)  # 21
                            data.append(abs(obj.s3d_e3_m - obj.s3d_e3_s))  # 22
                            data.append(
                                (abs(obj.s3d_e3_m - obj.s3d_e3_s) / obj.s3d_e3_s) * 100)  # 23

                            data.append(abs(obj.s3e_e1_m - obj.s3e_e1_s))  # 24
                            data.append(
                                (abs(obj.s3e_e1_m - obj.s3e_e1_s) / obj.s3e_e1_s) * 100)  # 25
                            data.append(abs(obj.s3e_e2_m - obj.s3e_e2_s))  # 26
                            data.append(
                                (abs(obj.s3e_e2_m - obj.s3e_e2_s) / obj.s3e_e2_s) * 100)  # 27
                            data.append(abs(obj.s3e_e3_m - obj.s3e_e3_s))  # 28
                            data.append(
                                (abs(obj.s3e_e3_m - obj.s3e_e3_s) / obj.s3e_e3_s) * 100)  # 29

                        elif (model == flowmeter_1):
                            template_name = 'report/flowmeter/licence1.html'
                            data.append(abs(int(obj.s1_e1_rlpm) - 0.5))  # 0
                            data.append(abs(int(obj.s1_e2_rlpm) - 2))  # 1
                            data.append(abs(int(obj.s1_e3_rlpm) - 4))  # 2
                            data.append(abs(int(obj.s1_e4_rlpm) - 7))  # 3
                            data.append(abs(int(obj.s1_e5_rlpm) - 10))  # 4
                            data.append(abs(int(obj.s1_e6_rlpm) - 15))  # 5
                            data.append(data[0] * 200)  # 6
                            data.append(data[1] * 50)  # 7
                            data.append(data[2] * 25)  # 8
                            data.append(round(data[3] * (100/7), 2))  # 9
                            data.append(data[4] * 10)  # 10
                            data.append(round(data[5] * (100/15), 2))  # 11

                        elif (model == infusion_pump_1):
                            template_name = 'report/infusion_pump/licence1.html'
                            data.append(abs((int(obj.s6_e1_mf) - 50)*2))  # 0
                            data.append(abs(int(obj.s6_e2_mf) - 100))  # 1

                        elif (model == monometer_1):
                            template_name = 'report/monometer/licence1.html'
                            data.append(abs(obj.s2_e1_sp - obj.s2_e1_np))  # 0
                            data.append(abs(obj.s2_e2_sp - obj.s2_e2_np))  # 1
                            data.append(abs(obj.s2_e3_sp - obj.s2_e3_np))  # 2
                            data.append(abs(obj.s2_e4_sp - obj.s2_e4_np))  # 3
                        elif (model == spo2_1):
                            template_name = 'report/spo2/licence1.html'
                            ss = 0
                            sss = 0
                            data.append((int(obj.s2_e1_spo2) - 70)**2)  # 0
                            data.append((int(obj.s2_e2_spo2) - 75)**2)  # 1
                            data.append((int(obj.s2_e3_spo2) - 80)**2)  # 2
                            data.append((int(obj.s2_e4_spo2) - 85)**2)  # 3
                            data.append((int(obj.s2_e5_spo2) - 88)**2)  # 4
                            data.append((int(obj.s2_e6_spo2) - 90)**2)  # 5
                            data.append((int(obj.s2_e7_spo2) - 92)**2)  # 6
                            data.append((int(obj.s2_e8_spo2) - 94)**2)  # 7
                            data.append((int(obj.s2_e9_spo2) - 96)**2)  # 8
                            data.append((int(obj.s2_e10_spo2) - 98)**2)  # 9
                            data.append((int(obj.s2_e11_spo2) - 100)**2)  # 10
                            for i in range(11):
                                ss += data[i]
                            data.append(int(((ss/11)**0.5)*100)/100)  # 11

                            data.append((int(obj.s3_e1_pr) - 35)**2)  # 12
                            data.append((int(obj.s3_e2_pr) - 60)**2)  # 13
                            data.append((int(obj.s3_e3_pr) - 100)**2)  # 14
                            data.append((int(obj.s3_e4_pr) - 200)**2)  # 15
                            data.append((int(obj.s3_e5_pr) - 240)**2)  # 16
                            for i in range(12, 17):
                                sss += data[i]
                            data.append(int(((sss/5)**0.5)*100)/100)  # 17

                        elif (model == suction_1):
                            template_name = 'report/suction/licence1.html'
                            data.append(abs(int(obj.s1_e1_rr)))  # 0
                            data.append(abs(int(obj.s1_e2_rr)))  # 1
                            data.append(abs(int(obj.s1_e3_rr) - 100))  # 2
                            data.append(abs(int(obj.s1_e4_rr) - 0.1))  # 3
                            data.append(abs(int(obj.s1_e5_rr) - 200))  # 4
                            data.append(abs(int(obj.s1_e6_rr - 0.3)))  # 5
                            data.append(abs(int(obj.s1_e7_rr) - 400))  # 6
                            data.append(abs(int(obj.s1_e8_rr) - 0.5))  # 7
                            data.append(abs(int(obj.s1_e9_rr) - 500))  # 8
                            data.append(abs(int(obj.s1_e10_rr) - 0.7))  # 9
                            data.append(abs(int(obj.s2_e1_rr)))  # 10/////
                            data.append(abs(int(obj.s2_e2_rr)))  # 11
                            data.append(abs(int(obj.s2_e2_rr) - 38))  # 12
                            data.append(abs(int(obj.s2_e2_rr) - 50))  # 13
                            data.append(abs(int(obj.s2_e2_rr) - 76))  # 14
                            data.append(abs(int(obj.s2_e2_rr) - 100))  # 15
                            data.append(abs(int(obj.s2_e2_rr) - 114))  # 16
                            data.append(abs(int(obj.s2_e2_rr) - 150))  # 17

                        elif (model == syringe_pump_1):
                            template_name = 'report/syringe_pump/licence1.html'
                            data.append(abs((int(obj.s6_e1_mf) - 50)*2))  # 0
                            data.append(abs(int(obj.s6_e2_mf) - 100))  # 1

                        elif (model == ventilator_1):
                            template_name = 'report/ventilator/licence1.html'
                            if obj.s16_e1 <= 550 and obj.s16_e1 >= 450:  # 0
                                data.append(1)
                            else:
                                data.append(0)
                            if obj.s16_e2 <= 13.2 and obj.s16_e2 >= 10.8:  # 1
                                data.append(1)
                            else:
                                data.append(0)
                            if obj.s16_1e1 != -1:  # 2
                                if obj.s16_e3 <= (obj.s16_1e1 * 1.1) and obj.s16_e3 >= (obj.s16_1e1 * 0.9):
                                    data.append(1)
                                else:
                                    data.append(0)
                            else:
                                data.append(2)
                            if obj.s16_1e2 != -1:  # 3
                                if obj.s16_e4 <= (obj.s16_1e2 * 1.1) and obj.s16_e4 >= (obj.s16_1e2 * 0.9):
                                    data.append(1)
                                else:
                                    data.append(0)
                            else:
                                data.append(2)
                            if obj.s16_e5 <= 0.55 and obj.s16_e5 >= 0.45:  # 4
                                data.append(1)
                            else:
                                data.append(0)
                            if obj.s16_e6 <= 22 and obj.s16_e6 >= 18:  # 5
                                data.append(1)
                            else:
                                data.append(0)
                            if obj.s16_1e3 != -1:  # 6
                                if obj.s16_e7 <= (obj.s16_1e3 * 1.1) and obj.s16_e7 >= (obj.s16_1e3 * 0.9):
                                    data.append(1)
                                else:
                                    data.append(0)
                            else:
                                data.append(2)
                        usr = aUserProfile.objects.get(user=obj.user)
                        t2 = jdatetime.datetime.today()
                        font_config = FontConfiguration()
                        html = render_to_string(template_name, {
                            'form': obj, 'time': t2, 'usr': usr, 'data': data, 'domain_name':domain_name})
                        print('\n\n\n\n\n\n\nhttp://{}{}'.format(domain_name, usr.signature.url))
                        css_root = static('/css')
                        css1 = CSS(
                            filename=f'{BASE_DIR}{css_root}/sop2-pdf.css')
                        css2 = CSS(
                            filename=f'{BASE_DIR}{css_root}/bootstrap-v4.min.css')
                        HTML(string=html).write_pdf(
                            'report.pdf', font_config=font_config, stylesheets=[css1, css2])
                        file.write(
                            f'{obj.licence.number} :: PDF fileCreated!\n')
    #===================================End-File Backing=================================================

    #===================================Begin-File Processing=================================================
                        lst = encode.objects.filter(
                            hospital=obj.device.hospital)
                        if len(lst) == 0:
                            filename = '12' + str(obj.device.hospital.user.id)
                            filename = hashlib.md5(
                                filename.encode()).hexdigest()
                            enc = encode.objects.create(
                                hospital=obj.device.hospital, name=filename)
                            enc.save()
                            encode_file.write('{}\n{}\n'.format(obj.device.hospital.name, filename))
                        else:
                            filename = lst[0].name

                
    #===================================Begin-FTP Stuf=================================================
                        ftp.cwd('pdf')
                        if not obj.device.hospital.city.state_name.eng_name in ftp.nlst():
                            ftp.mkd(obj.device.hospital.city.state_name.eng_name)
                        ftp.cwd(obj.device.hospital.city.state_name.eng_name)
                        if not obj.device.hospital.city.eng_name in ftp.nlst():
                            ftp.mkd(obj.device.hospital.city.eng_name)
                        ftp.cwd(obj.device.hospital.city.eng_name)
                        if not filename in ftp.nlst():
                            ftp.mkd(filename)
                        ftp.cwd(filename)
                        if not str(obj.request.number) in ftp.nlst():
                            ftp.mkd(str(obj.request.number))
                        ftp.cwd(str(obj.request.number))
                        if not str(obj.device.section.eng_name) in ftp.nlst():
                            ftp.mkd(str(obj.device.section.eng_name))
                        ftp.cwd(str(obj.device.section.eng_name))
                        if not modellist[s] in ftp.nlst():
                            ftp.mkd(modellist[s])
                        ftp.cwd(modellist[s])
                        try:
                            send_file_ftp(ftp, f'{obj.licence.number}.pdf')
                            file.write(
                                f'{obj.licence.number} :: File Successfully Uploaded!\n')
                        except:
                            file.write(
                                f'{obj.licence.number} :: An eeror occured while uploading to Host!\n')                        
                        ftp.cwd('..')
                        ftp.cwd('..')
                        ftp.cwd('..')
                        ftp.cwd('..')
                        ftp.cwd('..')
                        ftp.cwd('..')
                        ftp.cwd('..')
    #===================================End-FTP Stuf=================================================
                        a12 = report.objects.create(tt=ad_test_type0.objects.get(type=modellist[s]), device=obj.device,
                                                    request=obj.request, date=obj.date, user=obj.user, status=obj.status,
                                                    record=obj.record, licence=obj.licence, is_recal=obj.is_recal, ref_record=obj.ref_record,
                                                    is_done=obj.is_done, totalcomment=obj.totalcomment)
                        a12.save()
                        file.write(
                            f'{obj.licence.number} :: Report has been generated!\n')
                        # obj.delete()
                        file.write(
                            f'{obj.licence.number} :: Raw data has beed deleted!\n\n')

                s += 1
            ftp.close()
            file.close()
            encode_file.close()
            return HttpResponse('done :) ')
    else:
        raise Http404


def reportview(request):
    if request.method == 'GET':
        if Group.objects.get(name='hospital') in request.user.groups.all():
            data = report.objects.filter(licence__number=request.GET['licence_num']).filter(
                request__hospital__user__id__exact=request.user.id)
        else:
            data = report.objects.filter(
                licence__number=request.GET['licence_num'])
        if len(data) != 0:
            name = encode.objects.get(hospital=data[0].device.hospital)
            return redirect('https://{}/pdf/{}/{}/{}/{}/{}/{}/{}.pdf'.format(
                dl_domain_name, 
                data[0].request.hospital.city.state_name.name, 
                data[0].request.hospital.city.name,
                name.name,
                data[0].request.number,
                data[0].device.section.name,
                data[0].tt,
                data[0].licence.number
                ))

        raise Http404
    else:
        raise Http404
