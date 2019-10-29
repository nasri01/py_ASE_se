from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from acc.models import Request, ad_excel_arg, Parameters
from form.forms import *
from .forms import *
from django.contrib.auth.models import User, Group
import jdatetime
from django.template import RequestContext

color_scheme = Parameters.objects.get(name__exact='color').value

model_list = [monitor_spo2_1, monitor_ecg_1, monitor_nibp_1, monitor_safety_1, aed_1, anesthesia_machine_1,
              defibrilator_1,ecg_1, flowmeter_1, infusion_pump_1, monometer_1, spo2_1, suction_1, syringe_pump_1,
              ventilator_1, electrocauter_1 ]

modellist = ['monitor_spo2', 'monitor_ecg', 'monitor_nibp', 'monitor_safety', 'aed', 'anesthesia_machine',
             'defibrilator','ecg', 'flowmeter', 'infusion_pump', 'monometer', 'spo2', 'suction', 'syringe_pump',
             'ventilator', 'electrocauter' ]
             
form_list = [monitor_spO2_1_Form, monitor_ecg_1_Form, monitor_nibp_1_Form, monitor_safety_1_Form, aed_1_Form,
             anesthesia_machine_1_Form, defibrilator_1_Form, ecg_1_Form, flowmeter_1_Form, infusion_pump_1_Form,
             monometer_1_Form, spo2_1_Form, suction_1_Form, syringe_pump_1_Form, ventilator_1_Form, electrocauter_1_Form]


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'].lower(), password=request.POST['password'])
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
        return render(request, 'acc/admin/index.html', {'status': 'Welcome Back', 'flag': '1', 'auser': auser})

    elif request.user.groups.all()[0] == Group.objects.get(name='hospital'):

        # if (jdatetime.date.today().month < 10):
        #     mm = f'0{jdatetime.date.today().month}'
        # else:
        #     mm = jdatetime.date.today().month
        req = Request.objects.filter(hospital__user=request.user).order_by('date')

        for t in req:
            t.date = t.date.today()
        return render(request, 'acc/hospital/index.html',
                      {'status': 'خوش آمدید', 'flag': 1,  'request': req,'auser': auser})
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
    fr1 = ad_excel_arg.objects.all().order_by('order')
    listt = []
    for model in model_list:
        modelobj = model.objects.filter(is_done=False)
        listt.extend(modelobj)

    return render(request, 'acc/employee/recalibration_list.html', {'firstrow': fr1, 'data': listt})


# list of all records
def report_list(request):
    fr1 = ad_excel_arg.objects.all().order_by('order')
    data = []
    for model in model_list:
        modelobj = model.objects.all()
        data.extend(modelobj)

    return render(request, 'acc/employee/report_list.html', {'firstrow': fr1, 'data': data})


# Perepare the appropiate Edit form for Frame
def edit_report(request):
    if (request.method == 'GET'):
        auser = aUserProfile.objects.get(user=request.user)
        c = 0
        for form in form_list:
            modelobj = form.Meta.model.objects.filter(record__number=int(request.GET['record_num']))
            if (len(modelobj) == 1):
                form_type = form
                break
            c += 1
        form1 = form_type(instance=modelobj[0])
        edata = {'form': form1,
                 'form_type': modellist[c],
                 'record_num': modelobj[0].record.number,
                 'licence_num': modelobj[0].licence.number,
                 'auser':auser
                 }

        if (modelobj[0].is_recal == False):  # its calibration
            edata['edit'] = 1
        else:
            edata['edit_recal'] = 1
        return render(request, 'acc/employee/index.html', edata)


# Perepare the appropiate Recalibration form for Frame
def recal_report(request):
    if (request.method == 'GET'):
        c = 0
        for form in form_list:
            modelobj = form.Meta.model.objects.filter(record__number=int(request.GET['record_num'])).filter(
                is_done__exact=False)
            if (len(modelobj) == 1):
                form_type = form
                break
            c += 1

        form1 = form_type(instance=modelobj[0])

        rdata = {'recal': 1,
                 'form': form1,
                 'form_type': modellist[c],
                 'ref_record_num': modelobj[0].record.number,
                 'ref_licence_num': modelobj[0].licence.number
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


# def add_device(request):
#     form1 = add_device_Form
#     if(request.method=='POST'):
#         pass
#     else:
#
#         return render(request,'acc/employee/Add_Device.html',{'form':form1})

def handler_400(request, Exception):
    response = render_to_response(
        '/acc/400.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 400

    return response


def handler_403(request, Exception):
    response = render_to_response(
        '/acc/403.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 403

    return response


def handler_404(request, Exception):
    response = render_to_response(
        '/acc/404.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 404

    return response


def handler_500(request, Exception):
    response = render_to_response(
        '/acc/500.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 500

    return response
