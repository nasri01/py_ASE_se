from django.shortcuts import render ,Http404 ,redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import jdatetime , pytz
from .forms import *
from acc.models import licence , Cal_device ,Section ,All_Device , record ,aUserProfile
from django.contrib.auth.models import Group



diclist = [['monitor_spo2',monitor_spo2_1, monitor_spO2_1_Form ,3],
        ['monitor_ecg',monitor_ecg_1, monitor_ecg_1_Form ,3],
        ['monitor_nibp',monitor_nibp_1, monitor_nibp_1_Form ,3],
        ['monitor_safety',monitor_safety_1, monitor_safety_1_Form,3],
        ['aed',aed_1, aed_1_Form ,2],
        ['anesthesia_machine', anesthesia_machine_1, anesthesia_machine_1_Form,4],
        ['defibrilator', defibrilator_1, defibrilator_1_Form,4],
        ['ecg', ecg_1, ecg_1_Form,4],
        ['flowmeter', flowmeter_1, flowmeter_1_Form,1],
        ['infusion_pump', infusion_pump_1,  infusion_pump_1_Form,4],
        ['monometer', monometer_1, monometer_1_Form,3],
        ['spo2', spo2_1, spo2_1_Form,4],
        ['suction', suction_1,suction_1_Form,4],
        ['syringe_pump', syringe_pump_1, syringe_pump_1_Form,4],
        ['ventilator', ventilator_1,ventilator_1_Form,4],
        ['electrocauter', electrocauter_1, electrocauter_1_Form,5],
        ['cant_test', cant_test, cant_test_Form,5],
           ]

@login_required
def router(request):

    if request.user.groups.all()[0] == Group.objects.get(name='employee'):
        auser = aUserProfile.objects.get(user=request.user)
        for item in diclist:
            if request.GET['type'] == item[0]:
                form1 = item[2]
                    ############################pop up a confirmation
                return render(request, 'acc/employee/index.html',{'form': form1, 'form_type': item[0],'auser':auser})

    else:
        raise Http404


# def save_router(request,formtype):
#     if request.user.groups.all()[0] == Group.objects.get(name='employee'):
#         auser = aUserProfile.objects.get(user=request.user)
#         for item in diclist:
#             if formtype == item[0]:
#                 form1 = item[2](request.POST)
#                 if form1.is_valid():
#                     sform = form1.save(commit=False)
#                     sform.user = request.user
#                     sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))
#                     sform.record = record.objects.create(number=int(record.objects.last().number)+1)
#                     sform.is_recal = False
#                     sform.ref_record = record.objects.get(number=-1)
#                     # Cant Test Conditio
#                     if (request.POST['status'] == '4'):
#                         ln = -1
#                         sform.licence = licence.objects.create(number=ln)
#                     else:
#                         ln = int(licence.objects.order_by('number')[len(licence.objects.all())-1].number) + 1
#                         sform.licence = licence.objects.create(number=ln)
#                     if (request.POST['status'] == '1'):
#                         sform.is_done = True
#                     else:
#                         sform.is_done = False
#                     sform.cal_dev_1_cd = Cal_device.objects.get(id=request.POST['cal_dev1']).calibration_date
#                     sform.cal_dev_1_xd = Cal_device.objects.get(
#                         id=request.POST['cal_dev1']).calibration_Expire_date
#                     if (item[3] >= 2):
#                         sform.cal_dev_2_cd = Cal_device.objects.get(id=request.POST['cal_dev2']).calibration_date
#                         sform.cal_dev_2_xd = Cal_device.objects.get(
#                             id=request.POST['cal_dev2']).calibration_Expire_date
#                         if (item[3] >= 3):
#                             sform.cal_dev_3_cd = Cal_device.objects.get(id=request.POST['cal_dev3']).calibration_date
#                             sform.cal_dev_3_xd = Cal_device.objects.get(
#                                 id=request.POST['cal_dev3']).calibration_Expire_date
#                             if (item[3] >= 4):
#                                 sform.cal_dev_4_cd = Cal_device.objects.get(id=request.POST['cal_dev4']).calibration_date
#                                 sform.cal_dev_4_xd = Cal_device.objects.get(
#                                     id=request.POST['cal_dev4']).calibration_Expire_date
#                                 if (item[3] == 5):
#                                     sform.cal_dev_5_cd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_date
#                                     sform.cal_dev_5_xd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_Expire_date
#                     sform.save()
#                     form1.save_m2m()
#                     return render(request, 'acc/employee/index.html',
#                                   {'green_status': f'اطلاعات با موفقیت ذخیره شد! شماره گواهی:{ln}','auser':auser})
#                 else:  # form imcomplete
#                     return render(request, 'acc/employee/index.html',
#                                   {'form': form1, 'red_status': 'اطلاعات ناقص است!', 'form_type': item[0],'auser':auser})
#     else:
#         raise Http404

# def save_edit_router(request,formtype):
#     if request.user.groups.all()[0] == Group.objects.get(name='employee'):
#         auser = aUserProfile.objects.get(user=request.user)
#         for item in diclist:
#             if formtype==item[0]:
#                 data = item[1].objects.all().get(record__number=request.POST['record_num'])
#                 form1 = item[2](request.POST , instance=data)


#                 if form1.is_valid():
#                     sform = form1.save(commit=False)
#                     sform.user = request.user
#                     sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))

#                     # Cant Test Condition
#                     if (request.POST['status'] == '4'):#assign untestable
#                         ln = -1
#                         sform.licence = licence.objects.create(number=ln)

#                     elif(data.licence.number==-1):#assign a new one
#                         ln = int(licence.objects.order_by('number')[len(licence.objects.all()) - 1].number) + 1
#                         sform.licence = licence.objects.create(number=ln)
#                     else:#assign pervious one
#                         ln = data.licence.number


#                     if (request.POST['status'] == '1'):
#                         sform.is_done = True
#                     else:
#                         sform.is_done = False

#                     sform.cal_dev_1_cd = Cal_device.objects.get(id=request.POST['cal_dev1']).calibration_date
#                     sform.cal_dev_1_xd = Cal_device.objects.get(
#                         id=request.POST['cal_dev1']).calibration_Expire_date
#                     if (item[3] >= 2):
#                         sform.cal_dev_2_cd = Cal_device.objects.get(id=request.POST['cal_dev2']).calibration_date
#                         sform.cal_dev_2_xd = Cal_device.objects.get(
#                             id=request.POST['cal_dev2']).calibration_Expire_date
#                         if (item[3] >= 3):
#                             sform.cal_dev_3_cd = Cal_device.objects.get(id=request.POST['cal_dev3']).calibration_date
#                             sform.cal_dev_3_xd = Cal_device.objects.get(
#                                 id=request.POST['cal_dev3']).calibration_Expire_date
#                             if (item[3] >= 4):
#                                 sform.cal_dev_4_cd = Cal_device.objects.get(
#                                     id=request.POST['cal_dev4']).calibration_date
#                                 sform.cal_dev_4_xd = Cal_device.objects.get(
#                                     id=request.POST['cal_dev4']).calibration_Expire_date
#                                 if (item[3] == 5):
#                                     sform.cal_dev_5_cd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_date
#                                     sform.cal_dev_5_xd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_Expire_date
#                     sform.save()
#                     form1.save_m2m()
#                     return render(request, 'acc/employee/index.html',
#                                   {'green_status': f'اطلاعات با موفقیت ویرایش  شد! شماره گواهی:{ln}','auser':auser})

#                 else:  # form imcomplete
#                     return render(request, 'acc/employee/index.html',
#                                   {'form': form1, 'red_status': 'اطلاعات ناقص است!', item[0]: 1,'auser':auser})
#     else:
#         raise Http404


# def save_recal_router(request,formtype):
#     if request.user.groups.all()[0] == Group.objects.get(name='employee'):
#         auser = aUserProfile.objects.get(user=request.user)
#         for item in diclist:
#             if formtype == item[0]:

#                 ref_data = item[1].objects.get(record__number=request.POST['ref_record_num'])
#                 form1 = item[2](request.POST)

#                 if form1.is_valid():
#                     sform = form1.save(commit=False)
#                     sform.user = request.user
#                     sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))
#                     sform.record = record.objects.create(number=int(record.objects.last().number) + 1)
#                     sform.is_recal = True
#                     sform.ref_record = ref_data.record
#                     # Cant Test Condition

#                     if (request.POST['status'] == '4'):
#                         ln = -1
#                         sform.licence = licence.objects.create(number=ln)

#                     else:
#                         ln = int(licence.objects.order_by('number')[len(licence.objects.all()) - 1].number) + 1
#                         sform.licence = licence.objects.create(number=ln)

#                     if (request.POST['status'] == '1'):
#                         ref_data.is_done = True
#                         ref_data.save()

#                     sform.cal_dev_1_cd = Cal_device.objects.get(id=request.POST['cal_dev1']).calibration_date
#                     sform.cal_dev_1_xd = Cal_device.objects.get(
#                         id=request.POST['cal_dev1']).calibration_Expire_date
#                     if (item[3] >= 2):
#                         sform.cal_dev_2_cd = Cal_device.objects.get(id=request.POST['cal_dev2']).calibration_date
#                         sform.cal_dev_2_xd = Cal_device.objects.get(
#                             id=request.POST['cal_dev2']).calibration_Expire_date
#                         if (item[3] >= 3):
#                             sform.cal_dev_3_cd = Cal_device.objects.get(id=request.POST['cal_dev3']).calibration_date
#                             sform.cal_dev_3_xd = Cal_device.objects.get(
#                                 id=request.POST['cal_dev3']).calibration_Expire_date
#                             if (item[3] >= 4):
#                                 sform.cal_dev_4_cd = Cal_device.objects.get(
#                                     id=request.POST['cal_dev4']).calibration_date
#                                 sform.cal_dev_4_xd = Cal_device.objects.get(
#                                     id=request.POST['cal_dev4']).calibration_Expire_date
#                                 if (item[3] == 5):
#                                     sform.cal_dev_5_cd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_date
#                                     sform.cal_dev_5_xd = Cal_device.objects.get(
#                                         id=request.POST['cal_dev5']).calibration_Expire_date

#                     sform.save()
#                     form1.save_m2m()
#                     return render(request, 'acc/employee/index.html',
#                                   {'green_status': f'اطلاعات با موفقیت ذخیره شد! شماره گواهی ریکالیبراسیون:{ln}','auser':auser})

#                 else:  # form imcomplete
#                     return render(request, 'acc/employee/index.html',
#                                   {'form': form1, 'red_status': 'اطلاعات ناقص است!', 'form_type': item[0],'auser':auser})
#     else:
#         raise Http404


# def save_recal_edit_router(request,formtype):
    # if request.user.groups.all()[0] == Group.objects.get(name='employee'):
    #     auser = aUserProfile.objects.get(user=request.user)
    #     for item in diclist:
    #         if formtype == item[0]:

    #             data = item[1].objects.all().get(record__number=request.POST['record_num'])
    #             ref_data = item[1].objects.get(record=data.ref_record)
    #             form1 = item[2](request.POST,instance=data)

    #             if form1.is_valid():

    #                 sform = form1.save(commit=False)
    #                 sform.user = request.user
    #                 sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))
    #                 # Cant Test Condition

    #                 if (request.POST['status'] == '4'):
    #                     ln = -1
    #                     sform.licence = licence.objects.create(number=ln)
    #                 elif(data.status.id == 4):
    #                     ln = int(licence.objects.order_by('number')[len(licence.objects.all()) - 1].number) + 1
    #                     sform.licence = licence.objects.create(number=ln)
    #                 else:
    #                     ln = ref_data.licence.number
                    
                    
    #                 if (request.POST['status'] == '1'):
    #                     ref_data.is_done = True
    #                     ref_data.save()
    #                 else:
    #                     ref_data.is_done = False
    #                     ref_data.save()

    #                 sform.cal_dev_1_cd = Cal_device.objects.get(id=request.POST['cal_dev1']).calibration_date
    #                 sform.cal_dev_1_xd = Cal_device.objects.get(
    #                     id=request.POST['cal_dev1']).calibration_Expire_date
    #                 if (item[3] >= 2):
    #                     sform.cal_dev_2_cd = Cal_device.objects.get(id=request.POST['cal_dev2']).calibration_date
    #                     sform.cal_dev_2_xd = Cal_device.objects.get(
    #                         id=request.POST['cal_dev2']).calibration_Expire_date
    #                     if (item[3] >= 3):
    #                         sform.cal_dev_3_cd = Cal_device.objects.get(id=request.POST['cal_dev3']).calibration_date
    #                         sform.cal_dev_3_xd = Cal_device.objects.get(
    #                             id=request.POST['cal_dev3']).calibration_Expire_date
    #                         if (item[3] >= 4):
    #                             sform.cal_dev_4_cd = Cal_device.objects.get(
    #                                 id=request.POST['cal_dev4']).calibration_date
    #                             sform.cal_dev_4_xd = Cal_device.objects.get(
    #                                 id=request.POST['cal_dev4']).calibration_Expire_date
    #                             if (item[3] == 5):
    #                                 sform.cal_dev_5_cd = Cal_device.objects.get(
    #                                     id=request.POST['cal_dev5']).calibration_date
    #                                 sform.cal_dev_5_xd = Cal_device.objects.get(
    #                                     id=request.POST['cal_dev5']).calibration_Expire_date

    #                 sform.save()
    #                 form1.save_m2m()

    #                 return render(request, 'acc/employee/index.html',
    #                               {'green_status': f'اطلاعات با موفقیت ویرایش شد! شماره گواهی ریکالیبراسیون:{ln}','auser':auser})

    #             else:  # form imcomplete
    #                 return render(request, 'acc/employee/index.html',
    #                               {'form': form1, 'red_status': 'اطلاعات ناقص است!', 'form_type': item[0],'auser':auser})
    # else:
    #     raise Http404


def delete_report(request):
    model = record.objects.get(number=int(request.GET['record_num']))
    model.delete()

    return redirect('report_list')

def save_router(request,formtype):
    if request.user.groups.all()[0] == Group.objects.get(name='employee'):
        auser = aUserProfile.objects.get(user=request.user)
        for item in diclist:
            if formtype == item[0]:
                
                if request.POST['op_type'] == 'save':    
                    form1 = item[2](request.POST)
                
                elif request.POST['op_type'] == 'save_recal':
                    ref_data = item[1].objects.get(record__number=request.POST['ref_record_num'])
                    form1 = item[2](request.POST)
                
                elif request.POST['op_type'] == 'save_edit':
                    data = item[1].objects.all().get(record__number=request.POST['record_num'])
                    form1 = item[2](request.POST , instance=data)
                
                elif request.POST['op_type'] == 'save_edit_recal':
                    data = item[1].objects.all().get(record__number=request.POST['record_num'])
                    ref_data = item[1].objects.get(record=data.ref_record)
                    form1 = item[2](request.POST,instance=data)
                   
                   
                   
                if form1.is_valid():
                    sform = form1.save(commit=False)
                    sform.user = request.user
                    sform.date = jdatetime.datetime.now().astimezone(pytz.timezone('Asia/Tehran'))
                    sform.record = record.objects.create(number=int(record.objects.last().number)+1)
                    
                    if request.POST['op_type'] == 'save':    
                        sform.is_recal = False
                        sform.ref_record = record.objects.get(number=-1)
                        ln = int(licence.objects.order_by('number')[len(licence.objects.all())-1].number) + 1
                        sform.licence = licence.objects.create(number=ln)
                        if (request.POST['status'] == '1'):
                            sform.is_done = True
                        else:
                            sform.is_done = False
                        green_status = f'اطلاعات با موفقیت ذخیره شد! شماره گواهی:{ln}'

                    elif request.POST['op_type'] == 'save_edit':
                        ln = data.licence.number
                        if (request.POST['status'] == '1'):
                            sform.is_done = True
                        else:
                            sform.is_done = False
                        green_status = f'اطلاعات با موفقیت ویرایش  شد! شماره گواهی:{ln}'


                    elif request.POST['op_type'] == 'save_recal':
                        sform.is_recal = True
                        sform.is_done = True #always True
                        sform.ref_record = record.objects.get(number=request.POST['ref_record_num'])
                        ln = int(licence.objects.order_by('number')[len(licence.objects.all()) - 1].number) + 1
                        sform.licence = licence.objects.create(number=ln)
                        if (request.POST['status'] == '1'):
                            ref_data.is_done = True
                            ref_data.save()
                        green_status = f'اطلاعات با موفقیت ذخیره شد! شماره گواهی ریکالیبراسیون:{ln}'

                    elif request.POST['op_type'] == 'save_edit_recal':
                        if (request.POST['status'] == '1'):
                            ref_data.is_done = True
                            ref_data.save()
                    green_status = f'اطلاعات با موفقیت ویرایش شد! شماره گواهی ریکالیبراسیون:{ln}'


                    sform.cal_dev_1_cd = Cal_device.objects.get(id=request.POST['cal_dev1']).calibration_date
                    sform.cal_dev_1_xd = Cal_device.objects.get(
                        id=request.POST['cal_dev1']).calibration_Expire_date
                    if (item[3] >= 2):
                        sform.cal_dev_2_cd = Cal_device.objects.get(id=request.POST['cal_dev2']).calibration_date
                        sform.cal_dev_2_xd = Cal_device.objects.get(
                            id=request.POST['cal_dev2']).calibration_Expire_date
                        if (item[3] >= 3):
                            sform.cal_dev_3_cd = Cal_device.objects.get(id=request.POST['cal_dev3']).calibration_date
                            sform.cal_dev_3_xd = Cal_device.objects.get(
                                id=request.POST['cal_dev3']).calibration_Expire_date
                            if (item[3] >= 4):
                                sform.cal_dev_4_cd = Cal_device.objects.get(id=request.POST['cal_dev4']).calibration_date
                                sform.cal_dev_4_xd = Cal_device.objects.get(
                                    id=request.POST['cal_dev4']).calibration_Expire_date
                                if (item[3] == 5):
                                    sform.cal_dev_5_cd = Cal_device.objects.get(
                                        id=request.POST['cal_dev5']).calibration_date
                                    sform.cal_dev_5_xd = Cal_device.objects.get(
                                        id=request.POST['cal_dev5']).calibration_Expire_date
                        sform.save()
                        form1.save_m2m()


                    return render(request, 'acc/employee/index.html',
                                {'green_status': green_status,'auser':auser})
                else:  # form imcomplete
                    return render(request, 'acc/employee/index.html',
                                {'form': form1, 'red_status': 'اطلاعات ناقص است!', 'form_type': item[0],'auser':auser})
    else:
        raise Http404


