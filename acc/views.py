import jdatetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import Http404, redirect, render
from django.template import RequestContext

from acc.models import Hospital, Parameters, Request, ad_excel_arg
from form.forms import *
from report.models import report

from .forms import *

try:
    color_scheme = Parameters.objects.get(name__exact='color').value
except:
    color_scheme = '17a2b8'
fr1 = ad_excel_arg.objects.all().order_by('id')
# model_list = [MonitorSpo2_1, MonitorECG_1, MonitorNIBP_1, MonitorSafety_1, AED_1, AnesthesiaMachine_1,
#               Defibrilator_1, ECG_1, FlowMeter_1, InfusionPump_1, ManoMeter_1, Spo2_1, Suction_1, SyringePump_1,
#               Ventilator_1, ElectroCauter_1, CantTest, report]

# modellist = ['MonitorSpo2', 'MonitorECG', 'MonitorNIBP', 'MonitorSafety', 'AED', 'AnesthesiaMachine',
#              'Defibrilator', 'ECG', 'FlowMeter', 'InfusionPump', 'ManoMeter', 'spo2', 'Suction', 'SyringePump',
#              'Ventilator', 'ElectroCauter', 'CantTest']

# form_list = [MonitorSpo2_1_Form, MonitorECG_1_Form, MonitorNIBP_1_Form, MonitorSafety_1_Form, AED_1_Form,
#              AnesthesiaMachine_1_Form, Defibrilator_1_Form, ECG_1_Form, FlowMeter_1_Form, InfusionPump_1_Form,
#              ManoMeter_1_Form, spo2_1_Form, suction_1_Form, syringe_pump_1_Form, ventilator_1_Form, electrocauter_1_Form,
#              CantTest_Form]

diclist = [['MonitorSpo2', MonitorSpo2_1, MonitorSpo2_1_Form],
           ['MonitorECG', MonitorECG_1, MonitorECG_1_Form],
           ['MonitorNIBP', MonitorNIBP_1, MonitorNIBP_1_Form],
           ['MonitorSafety', MonitorSafety_1, MonitorSafety_1_Form],
           ['AED', AED_1, AED_1_Form],
           ['AnesthesiaMachine', AnesthesiaMachine_1,
               AnesthesiaMachine_1_Form],
           ['Defibrilator', Defibrilator_1, Defibrilator_1_Form],
           ['ECG', ECG_1, ECG_1_Form],
           ['FlowMeter', FlowMeter_1, FlowMeter_1_Form],
           ['InfusionPump', InfusionPump_1, InfusionPump_1_Form],
           ['ManoMeter', ManoMeter_1, ManoMeter_1_Form],
           ['spo2', Spo2_1, spo2_1_Form],
           ['Suction', Suction_1, suction_1_Form],
           ['SyringePump', SyringePump_1, syringe_pump_1_Form],
           ['Ventilator', Ventilator_1, ventilator_1_Form],
           ['ElectroCauter', ElectroCauter_1, electrocauter_1_Form],
           ['CantTest', CantTest, CantTest_Form],
           ['report', report],
           ]  # Order the same by ad_test_type0


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'].lower(), password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'acc/login.html',
                          {'error': 'نام کاربری یا رمز عبور اشتباه است!', 'color': color_scheme})
    elif request.user.is_anonymous:
        return render(request, 'acc/login.html', {'color': color_scheme})
    else:
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login1')


@login_required
def submit(request):
    auser = aUserProfile.objects.get(user=request.user)
    if Group.objects.get(name='admin') in request.user.groups.all():
        try:
            request.GET['employee']
            return render(request, 'acc/employee/index.html', {'status1': 'خوش آمدید', 'auser': auser})
        except:
            hospital_list = Hospital.objects.all()
            req = Request.objects.all().order_by('date')
            chart = [0, 0, 0, 0]
            for model in diclist:
                if model[1] == CantTest:
                    continue
                chart[0] += len(model[1].objects.filter(status__id=1))
                chart[1] += len(model[1].objects.filter(status__id=2))
                chart[2] += len(model[1].objects.filter(status__id=3))
            chart[3] = len(CantTest.objects.all())
            for t in req:
                t.date = t.date.today()

            return render(request, 'acc/admin/index.html', {
                'status': 'Welcome Back', 'flag': '1', 'auser': auser, 'hosplist': hospital_list, 'request': req,
                'chart': chart})

    elif Group.objects.get(name='hospital') in request.user.groups.all():

        req = Request.objects.filter(
            hospital__user=request.user).order_by('date')
        chart = [0, 0, 0, 0]
        for model in diclist:
            if model[1] == CantTest:
                continue
            query = model[1].objects.filter(
                device__hospital__user=request.user)

            chart[0] += len(query.filter(status__id=1))
            chart[1] += len(query.filter(status__id=2))
            chart[2] += len(query.filter(status__id=3))
        chart[3] = len(CantTest.objects.filter(
            device__hospital__user=request.user))
        for t in req:
            t.date = t.date.today()
        return render(request, 'acc/hospital/index.html',
                      {'status': 'خوش آمدید', 'flag': 1,  'request': req, 'auser': auser, 'chart': chart})
        #    'date': jdatetime.date.today(), 'month': mm,

    elif Group.objects.get(name='employee') in request.user.groups.all():
        return render(request, 'acc/employee/index.html', {'status1': 'خوش آمدید', 'auser': auser})


# list of requests
def req_list(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        req = Request.objects.all()
        for r in req:
            r.date = jdatetime.date.fromgregorian(date=r.date)
        return render(request, 'acc/employee/request_list.html', {'req': req})
    else:
        raise Http404

# List of recalibration


def recal_list(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        data = []
        data1 = []
        for model in diclist:
            modelobj = model[1].objects.filter(is_done=False)
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
                row.append(obj.device.property_number)  # 8
                row.append(obj.status.status)  # 9
                row.append(obj.date.strftime("%Y-%m-%d"))  # 10
                if obj.status.id != 4:
                    row.append(obj.licence.number)  # 11
                else:
                    row.append('-')  # 11
                row.append(obj.record.number)  # 12
                row.append(obj.status.id)  # 13
                data.append(row)

        return render(request, 'acc/employee/recalibration_list.html', {'firstrow': fr1, 'data': data})
    else:
        raise Http404

# list of all records


def report_list(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        data = []
        data1 = []
        for model in diclist[:-1]:
            modelobj = model[1].objects.all()
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
                row.append(obj.device.property_number)  # 8
                row.append(obj.status.status)  # 9
                row.append(obj.date.strftime("%Y-%m-%d"))  # 10
                if obj.status.id != 4:
                    row.append(obj.licence.number)  # 11
                else:
                    row.append('-')  # 11
                row.append(obj.record.number)  # 12
                data.append(row)
        return render(request, 'acc/employee/report_list.html', {'firstrow': fr1, 'data': data})
    else:
        raise Http404

# Perepare the appropiate Edit form for Frame


def edit_report(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        if (request.method == 'GET'):
            auser = aUserProfile.objects.get(user=request.user)
            for model in diclist:
                modelobj = model[2].Meta.model.objects.filter(
                    record__number=int(request.GET['record_num']))
                if (len(modelobj) == 1):
                    form_type = model[2]
                    form_type_str = model[0]
                    break

            try:
                form_type
            except:
                raise Http404
            form1 = form_type(instance=modelobj[0])
            edata = {'form': form1,
                     'form_type': form_type_str,
                     'record_num': modelobj[0].record.number,
                     'licence_num': modelobj[0].licence.number,
                     'auser': auser
                     }

            if (modelobj[0].is_recal == False):  # its calibration
                edata['edit'] = 1
            else:
                edata['edit_recal'] = 1
            return render(request, 'acc/employee/index.html', edata)
    else:
        raise Http404

# Perepare the appropiate Recalibration form for Frame


def recal_report(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        if (request.method == 'GET'):
            auser = aUserProfile.objects.get(user=request.user)
            for model in diclist:
                modelobj = model[1].objects.filter(record__number=int(request.GET['record_num'])).filter(
                    is_done__exact=False)

                if (len(modelobj) == 1):
                    if model[0] in ['CantTest', 'report']:
                        form_type = diclist[int(modelobj[0].tt.id)-1][2]
                        form_type_str = diclist[int(modelobj[0].tt.id)-1][0]
                    else:
                        form_type = model[2]
                        form_type_str = model[0]
                    break

            form1 = form_type({'device': [modelobj[0].device.id]})
            rdata = {'recal': 1,
                     'form': form1,
                     'form_type': form_type_str,
                     'ref_record_num': modelobj[0].record.number,
                     'auser': auser
                     }
            try:
                rdata['ref_licence_num'] = modelobj[0].licence.number
            except:
                pass
            return render(request, 'acc/employee/index.html', rdata)
    else:
        raise Http404


def make_done(request):
    if (request.method == 'GET'):
        query = CantTest.objects.filter(
            record__number=int(request.GET['record_num']))
        print(len(query))
        query[0].is_done = True
        query[0].save()

        return redirect('recal_list')
    else:
        raise Http404


@login_required
def change_email(request):
    if (request.method == 'POST'):
        if (request.POST['email1'] == request.POST['email2']):
            d = User.objects.get(id=request.user.id)
            d.email = request.POST['email1']
            d.save()
            return render(request, 'registration/email_change_done.html')
        else:
            return render(request, 'registration/email_change_form.html',
                          {'red_status': 'ایمیل ها مطابقت ندارند!'})
    else:
        return render(request, 'registration/email_change_form.html')
