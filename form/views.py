from django.shortcuts import render, Http404, redirect
from django.contrib.auth.decorators import login_required
import jdatetime
import pytz
from acc.models import Licence, CalDevice, Record, UserProfile
from .forms import *
from django.contrib.auth.models import Group


model_list = [['MonitorSpo2', MonitorSpo2_1, MonitorSpo2_1_Form, 3],
           ['MonitorECG', MonitorECG_1, MonitorECG_1_Form, 3],
           ['MonitorNIBP', MonitorNIBP_1, MonitorNIBP_1_Form, 3],
           ['MonitorSafety', MonitorSafety_1, MonitorSafety_1_Form, 3],
           ['AED', AED_1, AED_1_Form, 2],
           ['AnesthesiaMachine', AnesthesiaMachine_1,
               AnesthesiaMachine_1_Form, 4],
           ['Defibrilator', Defibrilator_1, Defibrilator_1_Form, 4],
           ['ECG', ECG_1, ECG_1_Form, 4],
           ['FlowMeter', FlowMeter_1, FlowMeter_1_Form, 1],
           ['InfusionPump', InfusionPump_1, InfusionPump_1_Form, 4],
           ['ManoMeter', ManoMeter_1, ManoMeter_1_Form, 3],
           ['spo2', Spo2_1, spo2_1_Form, 4],
           ['Suction', Suction_1, suction_1_Form, 4],
           ['SyringePump', SyringePump_1, syringe_pump_1_Form, 4],
           ['Ventilator', Ventilator_1, ventilator_1_Form, 4],
           ['ElectroCauter', ElectroCauter_1, electrocauter_1_Form, 5],
           ['CantTest', CantTest, CantTest_Form, 0],
           ]


@login_required
def router(request):

    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        auser = UserProfile.objects.get(user=request.user)
        for item in model_list:
            if request.GET['type'] == item[0]:
                form1 = item[2]
                # pop up a confirmation
                return render(request, 'acc/employee/index.html', {'form': form1, 'form_type': item[0], 'auser': auser, })
    else:
        raise Http404


def delete_report(request):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        for model in model_list:
            modelobj = model[1].objects.filter(
                record__number=int(request.GET['record_num']))
            if len(modelobj) == 1:
                modelobj[0].delete()
                break

        return redirect('report_list')
    else:
        raise Http404

def save_router(request, formtype):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        auser = UserProfile.objects.get(user=request.user)
        for item in model_list:
            if formtype == item[0]:

                if request.POST['op_type'] == 'save':
                    form1 = item[2](request.POST)

                elif request.POST['op_type'] == 'save_recal':
                    ref_data = item[1].objects.get(
                        record__number=request.POST['ref_record_num'])
                    form1 = item[2](request.POST)

                elif request.POST['op_type'] == 'save_edit':
                    data = item[1].objects.all().get(
                        record__number=request.POST['record_num'])
                    form1 = item[2](request.POST, instance=data)

                elif request.POST['op_type'] == 'save_edit_recal':
                    data = item[1].objects.all().get(
                        record__number=request.POST['record_num'])
                    ref_data = item[1].objects.get(Record=data.ref_record)
                    form1 = item[2](request.POST, instance=data)
                else:
                    form1 = item[2](request.POST)

                if form1.is_valid():
                    sform = form1.save(commit=False)
                    sform.user = request.user
                    sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))
                    sform.Record = Record.objects.create(
                        number=int(Record.objects.last().number)+1)

                    if request.POST['op_type'] == 'save':
                        sform.is_recal = False
                        sform.ref_record = Record.objects.get(number=-1)
                        if item[0] != 'CantTest':
                            ln = int(Licence.objects.order_by('number')[
                                len(Licence.objects.all())-1].number) + 1
                            sform.Licence = Licence.objects.create(number=ln)
                        else:
                            ln = -1

                        if (request.POST['status'] == '1'):
                            sform.is_done = True
                        else:
                            sform.is_done = False
                        green_status = f'اطلاعات {item[0]} با موفقیت ذخیره شد! شماره گواهی:{ln}'

                    elif request.POST['op_type'] == 'save_edit':
                        ln = data.Licence.number
                        if (request.POST['status'] == '1'):
                            sform.is_done = True
                        else:
                            sform.is_done = False
                        green_status = f'اطلاعات با موفقیت ویرایش  شد! شماره گواهی:{ln}'

                    elif request.POST['op_type'] == 'save_recal':
                        sform.is_recal = True
                        sform.is_done = True  # always True
                        sform.ref_record = Record.objects.get(
                            number=request.POST['ref_record_num'])
                        ln = int(Licence.objects.order_by('number')[
                                 len(Licence.objects.all()) - 1].number) + 1
                        sform.Licence = Licence.objects.create(number=ln)
                        if (request.POST['status'] == '1'):
                            ref_data.is_done = True
                            ref_data.save()
                        green_status = f'اطلاعات با موفقیت ذخیره شد! شماره گواهی ریکالیبراسیون:{ln}'

                    elif request.POST['op_type'] == 'save_edit_recal':
                        ln = data.Licence.number
                        if (request.POST['status'] == '1'):
                            ref_data.is_done = True
                        elif request.POST['status'] != '1':
                            ref_data.is_done = False
                        ref_data.save()
                        green_status = f'اطلاعات با موفقیت ویرایش شد! شماره گواهی ریکالیبراسیون:{ln}'
                    else:
                        green_status = f'اطلاعات با موفقیت ذخیره شد!'

                    if (item[3] != 0):
                        sform.cal_dev_1_cd = CalDevice.objects.get(
                            id=request.POST['cal_dev1']).calibration_date
                        sform.cal_dev_1_xd = CalDevice.objects.get(
                            id=request.POST['cal_dev1']).calibration_Expire_date
                        if (item[3] >= 2):
                            sform.cal_dev_2_cd = CalDevice.objects.get(
                                id=request.POST['cal_dev2']).calibration_date
                            sform.cal_dev_2_xd = CalDevice.objects.get(
                                id=request.POST['cal_dev2']).calibration_Expire_date
                            if (item[3] >= 3):
                                sform.cal_dev_3_cd = CalDevice.objects.get(
                                    id=request.POST['cal_dev3']).calibration_date
                                sform.cal_dev_3_xd = CalDevice.objects.get(
                                    id=request.POST['cal_dev3']).calibration_Expire_date
                                if (item[3] >= 4):
                                    sform.cal_dev_4_cd = CalDevice.objects.get(
                                        id=request.POST['cal_dev4']).calibration_date
                                    sform.cal_dev_4_xd = CalDevice.objects.get(
                                        id=request.POST['cal_dev4']).calibration_Expire_date
                                    if (item[3] == 5):
                                        sform.cal_dev_5_cd = CalDevice.objects.get(
                                            id=request.POST['cal_dev5']).calibration_date
                                        sform.cal_dev_5_xd = CalDevice.objects.get(
                                            id=request.POST['cal_dev5']).calibration_Expire_date
                    sform.save()

                    return render(request, 'acc/employee/index.html',
                                  {'green_status': green_status, 'auser': auser})
                else:  # form imcomplete
                    return render(request, 'acc/employee/index.html',
                                  {'form': form1, 'red_status': 'اطلاعات ناقص است!', 'form_type': item[0], 'auser': auser})
    else:
        raise Http404


def reload(request, formtype):
    if Group.objects.get(name='admin') in request.user.groups.all() or Group.objects.get(name='employee') in request.user.groups.all():
        auser = UserProfile.objects.get(user=request.user)
        for item in model_list:
            if formtype == item[0]:
                form1 = item[2](request.POST)
                return render(request, 'acc/employee/index.html',
                              {'form': form1, 'form_type': item[0], 'auser': auser, 'reload': 1})
