import io
import pytz
import xlsxwriter
import jdatetime
import os
from jdatetime import timedelta
from form.models import *
from .models import report


from acc.models import ad_excel_arg, aUserProfile, Request, device_type, ad_test_type0

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User, Group
from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.template.loader import render_to_string




model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, defibrilator_1, aed_1, ecg_1,
              infusion_pump_1, syringe_pump_1, spo2_1, flowmeter_1, anesthesia_machine_1, ventilator_1,
              suction_1, electrocauter_1, monometer_1, cant_test, report]
modellist = ['monitor Spo2', 'monitor ECG', 'monitor NIBP', 'monitor Safety', 'Defibrilator', 'AED', 'ECG',
             'Infusion Pump', 'Syringe Pump', 'Pulse Oximetry', 'Flow Meter', 'Anesthesia Machine', 'Ventilator',
             'Suction', 'ElectroCouter', 'Mano Meter', 'cant_test']


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
            if request.user.groups.all()[0] == Group.objects.get(name='admin'):  # admin
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
            if request.user.groups.all()[0] != Group.objects.get(name='admin'):
                for model in model_list:
                    modelobj = model.objects.filter(date__gte=start).filter(date__lte=end).filter(
                        request__hospital__user__id__exact=request.user.id)
                    data1.append(modelobj)
            else:
                for model in model_list:
                    modelobj = model.objects.filter(
                        date__gte=start).filter(date__lte=end)
                    data1.append(modelobj)

        for obj1 in data1:
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
                         str(fr1[15])
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
                        idata[12],
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