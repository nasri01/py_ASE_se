from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render, Http404
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
# model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, aed_1, anesthesia_machine_1,
#               defibrilator_1, ecg_1, flowmeter_1, infusion_pump_1, monometer_1, spo2_1, suction_1, syringe_pump_1,
#               ventilator_1, electrocauter_1, cant_test, report]

# modellist = ['monitor_spo2', 'monitor_ecg', 'monitor_nibp', 'monitor_safety', 'aed', 'anesthesia_machine',
#              'defibrilator', 'ecg', 'flowmeter', 'infusion_pump', 'monometer', 'spo2', 'suction', 'syringe_pump',
#              'ventilator', 'electrocauter', 'cant_test']

# form_list = [monitor_spO2_1_Form, monitor_ecg_1_Form, monitor_nibp_1_Form, monitor_safety_1_Form, aed_1_Form,
#              anesthesia_machine_1_Form, defibrilator_1_Form, ecg_1_Form, flowmeter_1_Form, infusion_pump_1_Form,
#              monometer_1_Form, spo2_1_Form, suction_1_Form, syringe_pump_1_Form, ventilator_1_Form, electrocauter_1_Form,
#              cant_test_Form]

diclist = [['monitor_spo2', monitor_spo2_1, monitor_spO2_1_Form],
           ['monitor_ecg', monitor_ecg_1, monitor_ecg_1_Form],
           ['monitor_nibp', monitor_nibp_1, monitor_nibp_1_Form],
           ['monitor_safety', monitor_safety_1, monitor_safety_1_Form],
           ['aed', aed_1, aed_1_Form],
           ['anesthesia_machine', anesthesia_machine_1,
               anesthesia_machine_1_Form],
           ['defibrilator', defibrilator_1, defibrilator_1_Form],
           ['ecg', ecg_1, ecg_1_Form],
           ['flowmeter', flowmeter_1, flowmeter_1_Form],
           ['infusion_pump', infusion_pump_1, infusion_pump_1_Form],
           ['monometer', monometer_1, monometer_1_Form],
           ['spo2', spo2_1, spo2_1_Form],
           ['suction', suction_1, suction_1_Form],
           ['syringe_pump', syringe_pump_1, syringe_pump_1_Form],
           ['ventilator', ventilator_1, ventilator_1_Form],
           ['electrocauter', electrocauter_1, electrocauter_1_Form],
           ['cant_test', cant_test, cant_test_Form],
           ['report', report],
           ]


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
    if request.user.groups.all()[0] == Group.objects.get(name='admin'):
        hospital_list = Hospital.objects.all()
        req = Request.objects.all().order_by('date')
        chart = [0, 0, 0, 0]
        for model in model_list:
            if model == cant_test:
                continue
            chart[0] += len(model.objects.filter(status__id=1))
            chart[1] += len(model.objects.filter(status__id=2))
            chart[2] += len(model.objects.filter(status__id=3))
        chart[3] = len(cant_test.objects.all())
        for t in req:
            t.date = t.date.today()

        return render(request, 'acc/admin/index.html', {
            'status': 'Welcome Back', 'flag': '1', 'auser': auser, 'hosplist': hospital_list, 'request': req,
            'chart': chart})

    elif request.user.groups.all()[0] == Group.objects.get(name='hospital'):

        req = Request.objects.filter(
            hospital__user=request.user).order_by('date')
        chart = [0, 0, 0, 0]
        for model in diclist:
            if model[1] == cant_test:
                continue
            query = model[1].objects.filter(
                device__hospital__user=request.user)

            chart[0] += len(query.filter(status__id=1))
            chart[1] += len(query.filter(status__id=2))
            chart[2] += len(query.filter(status__id=3))
        chart[3] = len(cant_test.objects.filter(
            device__hospital__user=request.user))
        for t in req:
            t.date = t.date.today()
        return render(request, 'acc/hospital/index.html',
                      {'status': 'خوش آمدید', 'flag': 1,  'request': req, 'auser': auser, 'chart': chart})
        #    'date': jdatetime.date.today(), 'month': mm,

    elif request.user.groups.all()[0] == Group.objects.get(name='employee'):
        return render(request, 'acc/employee/index.html', {'status1': 'خوش آمدید', 'auser': auser})


# list of requests
def req_list(request):
    req = Request.objects.all()

    for t in req:
        t.date = t.date.today()

    return render(request, 'acc/employee/request_list.html', {'req': req})


# List of recalibration
def recal_list(request):
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
                print(obj.status.id)
                row.append(obj.licence.number)  # 11
            else:
                row.append('-')  # 11
            row.append(obj.record.number)  # 12
            data.append(row)

    return render(request, 'acc/employee/recalibration_list.html', {'firstrow': fr1, 'data': data})


# list of all records
def report_list(request):
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
                if obj.licence.number != -1:
                    row.append(obj.licence.number)  # 11
                else:
                    row.append('-')  # 11
            row.append(obj.record.number)  # 12
            data.append(row)
    return render(request, 'acc/employee/report_list.html', {'firstrow': fr1, 'data': data})


# Perepare the appropiate Edit form for Frame
def edit_report(request):
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


# Perepare the appropiate Recalibration form for Frame
def recal_report(request):
    if (request.method == 'GET'):
        auser = aUserProfile.objects.get(user=request.user)
        for model in diclist:
            modelobj = model[2].Meta.model.objects.filter(record__number=int(request.GET['record_num'])).filter(
                is_done__exact=False)
            if (len(modelobj) == 1):
                form_type = model[2]
                form_type_str = model[0]
                break

        form1 = form_type(instance=modelobj[0])

        rdata = {'recal': 1,
                 'form': form1,
                 'form_type': form_type_str,
                 'ref_record_num': modelobj[0].record.number,
                 'ref_licence_num': modelobj[0].licence.number,
                 'auser': auser
                 }

        return render(request, 'acc/employee/index.html', rdata)


def change_email(request):
    if (request.method == 'POST'):
        if (request.POST['email1'] == request.POST['email2']):
            d = User.objects.get(id=request.user.id)
            d.email = request.POST['email1']
            d.save()
            return render(request, 'acc/employee/index.html',
                          {'settings': 1, 'change_email': 1, 'change_email_done': 1, })
        else:
            return render(request, 'acc/employee/index.html',
                          {'settings': 1, 'change_email': 1, 'red_status': 'ایمیل ها مطابقت ندارند!', 'form': 1})
    else:
        return render(request, 'acc/employee/index.html', {'settings': 1, 'change_email': 1, 'form': 1})
