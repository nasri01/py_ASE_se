from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from acc.models import Request, excel_arg ,Parameters
from form.forms import *
from .forms import *
from django.contrib.auth.models import User
import jdatetime

#color_scheme = Parameters.objects.get(name__exact='color').value
color_scheme = 2 #test



model_list = [monitor_spo2_1,monitor_ecg_1,monitor_nibp_1,aed_1,monitor_safety_1,anesthesia_machine_1,defibrilator_1,]


modellist = ['monitor_spo2', 'monitor_ecg', 'monitor_nibp', 'aed','monitor_safety','anesthesia_machine','defibrilator',]
form_list = [monitor_spO2_1_Form,monitor_ecg_1_Form,monitor_nibp_1_Form,aed_1_Form,monitor_safety_1_Form,anesthesia_machine_1_Form,defibrilator_1_Form]



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'].lower(), password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'acc/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است!','color':color_scheme})
    elif request.user.is_anonymous:
        return render(request, 'acc/login.html',{'color':color_scheme})
    else:
        return redirect('dashboard')
def logout(request):
    auth.logout(request)
    return redirect('login1')

@login_required
def submit(request):
    if request.user.last_name == 'admin':
        return render(request, 'acc/admin/index.html', {'status': 'Welcome Back', 'flag': '1'})

    elif request.user.last_name == 'hospital':
        if (jdatetime.date.today().month < 10):
            mm = f'0{jdatetime.date.today().month}'
        else:
            mm = jdatetime.date.today().month
        req = Request.objects.filter(hospital__user = request.user).order_by('date')
        return render(request, 'acc/hospital/index.html',
                      {'status': 'خوش آمدید', 'flag': 1, 'date': jdatetime.date.today(), 'month': mm,'request':req})

    elif request.user.last_name == 'employee':
        return render(request, 'acc/employee/index.html', {'status1': 'خوش آمدید'})


# list of requests
def req_list(request):
    model = Request.objects.all()

    return render(request, 'acc/employee/request_list.html', {'model': model})
# List of recalibration
def recal_list(request):
    fr1 = excel_arg.objects.all().order_by('order')
    listt = []
    for model in model_list:
        modelobj = model.objects.filter(is_done=False)
        listt.extend(modelobj)

    return render(request, 'acc/employee/recalibration_list.html', {'firstrow': fr1, 'data': listt})
# list of all records
def report_list(request):
    fr1 = excel_arg.objects.all().order_by('order')
    data = []
    for model in model_list:
        modelobj = model.objects.all()
        data.extend(modelobj)

    return render(request, 'acc/employee/report_list.html', {'firstrow': fr1, 'data': data})


# Perepare the appropiate Edit form for Frame
def edit_report(request):
    if (request.method == 'GET'):
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
                 'licence_num': modelobj[0].licence.number
                 }
        
        if (modelobj[0].is_recal == False):  # its calibration
            edata['edit'] = 1
        else:
            edata['edit_recal'] = 1
        return render(request, 'acc/employee/index.html', edata)


# Perepare the appropiate Recalibration form for Frame
def recal_report(request):
    if (request.method == 'GET'):
        c=0
        for form in form_list:
            modelobj = form.Meta.model.objects.filter(record__number=int(request.GET['record_num'])).filter(is_done__exact=False)
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
    if(request.method=='POST'):
        if(request.POST['email1']==request.POST['email2']):
            d = User.objects.get(id=request.user.id)
            d.email = request.POST['email1']
            d.save()
            return render(request, 'acc/employee/index.html', {'settings':1,'change_email': 1, 'change_email_done': 1, })
        else:
            return render(request, 'acc/employee/index.html',
                          {'settings':1,'change_email': 1, 'red_status': 'ایمیل ها مطابقت ندارند!', 'form': 1})
    else:
        return render(request, 'acc/employee/index.html', {'settings':1,'change_email': 1, 'form': 1})


def add_device(request):
    form1 = add_device_Form
    if(request.method=='POST'):
        pass
    else:

        return render(request,'acc/employee/Add_Device.html',{'form':form1})
