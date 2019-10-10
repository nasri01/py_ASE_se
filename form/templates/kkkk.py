from django.db import models

import acc.models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

class monitor_spo2_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='ms1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_spo2,related_name='ms1totalcomment')
    is_done = models.BooleanField(default=False)


    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='ms1caldev1',default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='ms1caldev2',default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='ms1caldev3',default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_status = models.BooleanField(default=False)
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='ms1s1e1comment')
    s1_e2_status = models.BooleanField(default=False)
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='ms11s1e2comment')

    s2_e1_spo2 = models.IntegerField()
    s2_e1_pr = models.IntegerField()
    s2_e2_spo2 = models.IntegerField()
    s2_e2_pr = models.IntegerField()
    s2_e3_spo2 = models.IntegerField()
    s2_e3_pr = models.IntegerField()
    s2_e4_spo2 = models.IntegerField()
    s2_e4_pr = models.IntegerField()
    s2_e5_spo2 = models.IntegerField()
    s2_e5_pr = models.IntegerField()
    s2_e6_spo2 = models.IntegerField()
    s2_e6_pr = models.IntegerField()
    s2_e7_spo2 = models.IntegerField()
    s2_e7_pr = models.IntegerField()
    s2_e8_spo2 = models.IntegerField()
    s2_e8_pr = models.IntegerField()
    s2_e9_spo2 = models.IntegerField()
    s2_e9_pr = models.IntegerField()
    s2_e10_spo2 = models.IntegerField()
    s2_e10_pr = models.IntegerField()
    s2_e11_spo2 = models.IntegerField()
    s2_e11_pr = models.IntegerField()

    s3_e1_spo2 = models.IntegerField()
    s3_e1_pr = models.IntegerField()
    s3_e2_spo2 = models.IntegerField()
    s3_e2_pr = models.IntegerField()
    s3_e3_spo2 = models.IntegerField()
    s3_e3_pr = models.IntegerField()
    s3_e4_spo2 = models.IntegerField()
    s3_e4_pr = models.IntegerField()
    s3_e5_spo2 = models.IntegerField()
    s3_e5_pr = models.IntegerField()

    s4_e1_acc = models.ForeignKey(acc.models.accessory,on_delete=models.PROTECT, related_name='ms1s4e1accessory')
    s4_e1_status = models.BooleanField(default=False)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='ms1s4e1comment')





    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_monitor_spo2_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rms1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rms1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_spo2)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='rms1caldev1',default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rms1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rms1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()



    s1_e1_status = models.BooleanField(default=False)
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='rms1s1s1e1comment')
    s1_e2_status = models.BooleanField(default=False)
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='rms1s1s1e2comment')

    s2_e1_spo2 = models.IntegerField()
    s2_e1_pr = models.IntegerField()
    s2_e2_spo2 = models.IntegerField()
    s2_e2_pr = models.IntegerField()
    s2_e3_spo2 = models.IntegerField()
    s2_e3_pr = models.IntegerField()
    s2_e4_spo2 = models.IntegerField()
    s2_e4_pr = models.IntegerField()
    s2_e5_spo2 = models.IntegerField()
    s2_e5_pr = models.IntegerField()
    s2_e6_spo2 = models.IntegerField()
    s2_e6_pr = models.IntegerField()
    s2_e7_spo2 = models.IntegerField()
    s2_e7_pr = models.IntegerField()
    s2_e8_spo2 = models.IntegerField()
    s2_e8_pr = models.IntegerField()
    s2_e9_spo2 = models.IntegerField()
    s2_e9_pr = models.IntegerField()
    s2_e10_spo2 = models.IntegerField()
    s2_e10_pr = models.IntegerField()
    s2_e11_spo2 = models.IntegerField()
    s2_e11_pr = models.IntegerField()

    s3_e1_spo2 = models.IntegerField()
    s3_e1_pr = models.IntegerField()
    s3_e2_spo2 = models.IntegerField()
    s3_e2_pr = models.IntegerField()
    s3_e3_spo2 = models.IntegerField()
    s3_e3_pr = models.IntegerField()
    s3_e4_spo2 = models.IntegerField()
    s3_e4_pr = models.IntegerField()
    s3_e5_spo2 = models.IntegerField()
    s3_e5_pr = models.IntegerField()

    s4_e1_acc = models.ForeignKey(acc.models.accessory,on_delete=models.PROTECT, related_name='rms1s4e1accessory')
    s4_e1_status = models.BooleanField(default=False)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2,on_delete=models.PROTECT, related_name='rms1s4e1comment')







    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class monitor_ecg_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='me1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_ecg)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='me1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='me1caldev2',default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='me1caldev3',default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_hr = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e1comment')
    s1_e2_hr = models.IntegerField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e2comment')
    s1_e3_hr = models.IntegerField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e3comment')
    s1_e4_hr = models.IntegerField()
    s1_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e4comment')
    s1_e5_hr = models.IntegerField()
    s1_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e5comment')
    s1_e6_hr = models.IntegerField()
    s1_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e6comment')
    s1_e7_hr = models.IntegerField()
    s1_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e7comment')
    s1_e8_hr = models.IntegerField()
    s1_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s1e8comment')

    s2_e1_hr = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e1comment')
    s2_e2_hr = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e2comment')
    s2_e3_hr = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e3comment')
    s2_e4_hr = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e4comment')
    s2_e5_hr = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e5comment')
    s2_e6_hr = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e6comment')
    s2_e7_hr = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e7comment')
    s2_e8_hr = models.IntegerField()
    s2_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e8comment')
    s2_e9_hr = models.IntegerField()
    s2_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e9comment')
    s2_e10_hr = models.IntegerField()
    s2_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s2e10comment')

    s3_e1_hr = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e1comment')
    s3_e2_hr = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e2comment')
    s3_e3_hr = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e3comment')
    s3_e4_hr = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e4comment')
    s3_e5_hr = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e5comment')
    s3_e6_hr = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e6comment')
    s3_e7_hr = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e7comment')
    s3_e8_hr = models.IntegerField()
    s3_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e8comment')
    s3_e9_hr = models.IntegerField()
    s3_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e9comment')
    s3_e10_hr = models.IntegerField()
    s3_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s3e10comment')
    s3_e11_hr = models.IntegerField()
    s3_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg, on_delete=models.PROTECT,
                                       related_name='me1s3e11comment')
    s3_e12_hr = models.IntegerField()
    s3_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg, on_delete=models.PROTECT,
                                       related_name='me1s3e12comment')

    s4_e1_hr = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s4e1comment')

    s5_e1_status = models.BooleanField(default=False)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s5e1comment')
    s5_e2_delay = models.FloatField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s5e2comment')
    s5_e3_delay = models.FloatField()
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s5e3comment')
    s5_e4_delay = models.FloatField()
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s5e4comment')

    s6_e1_damp = models.FloatField()
    s6_e1_Ramp = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s6e1comment')
    s6_e2_damp = models.FloatField()
    s6_e2_Ramp = models.FloatField()
    s6_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s6e2comment')
    s6_e3_damp = models.FloatField()
    s6_e3_Ramp = models.FloatField()
    s6_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s6e3comment')

    s7_e1_damp = models.FloatField()
    s7_e1_Ramp = models.FloatField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s7e1comment')
    s7_e2_damp = models.FloatField()
    s7_e2_Ramp = models.FloatField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s7e2comment')
    s7_e3_damp = models.FloatField()
    s7_e3_Ramp = models.FloatField()
    s7_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s7e3comment')
    s7_e4_damp = models.FloatField()
    s7_e4_Ramp = models.FloatField()
    s7_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s7e4comment')
    s7_e5_damp = models.FloatField()
    s7_e5_Ramp = models.FloatField()
    s7_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s7e5comment')

    s8_e1_bdisp = models.FloatField()
    s8_e1_slope = models.FloatField()
    s8_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s8e1comment')

    s9_e1_status = models.BooleanField(default=False)
    s9_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='me1s9e1comment')





    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_monitor_ecg_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rme1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rme1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_ecg)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='rme1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rme1caldev2',default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rme1caldev3',default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()


    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e1comment')
    s1_e2_hr = models.IntegerField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e2comment')
    s1_e3_hr = models.IntegerField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e3comment')
    s1_e4_hr = models.IntegerField()
    s1_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e4comment')
    s1_e5_hr = models.IntegerField()
    s1_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e5comment')
    s1_e6_hr = models.IntegerField()
    s1_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e6comment')
    s1_e7_hr = models.IntegerField()
    s1_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e7comment')
    s1_e8_hr = models.IntegerField()
    s1_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s1e8comment')

    s2_e1_hr = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e1comment')
    s2_e2_hr = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e2comment')
    s2_e3_hr = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e3comment')
    s2_e4_hr = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e4comment')
    s2_e5_hr = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e5comment')
    s2_e6_hr = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e6comment')
    s2_e7_hr = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e7comment')
    s2_e8_hr = models.IntegerField()
    s2_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e8comment')
    s2_e9_hr = models.IntegerField()
    s2_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e9comment')
    s2_e10_hr = models.IntegerField()
    s2_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s2e10comment')

    s3_e1_hr = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e1comment')
    s3_e2_hr = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e2comment')
    s3_e3_hr = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e3comment')
    s3_e4_hr = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e4comment')
    s3_e5_hr = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e5comment')
    s3_e6_hr = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e6comment')
    s3_e7_hr = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e7comment')
    s3_e8_hr = models.IntegerField()
    s3_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e8comment')
    s3_e9_hr = models.IntegerField()
    s3_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e9comment')
    s3_e10_hr = models.IntegerField()
    s3_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s3e10comment')
    s3_e11_hr = models.IntegerField()
    s3_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg, on_delete=models.PROTECT,
                                       related_name='rme1s3e11comment')
    s3_e12_hr = models.IntegerField()
    s3_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg, on_delete=models.PROTECT,
                                       related_name='rme1s3e12comment')

    s4_e1_hr = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s4e1comment')

    s5_e1_status = models.BooleanField(default=False)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s5e1comment')
    s5_e2_delay = models.FloatField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s5e2comment')
    s5_e3_delay = models.FloatField()
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s5e3comment')
    s5_e4_delay = models.FloatField()
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s5e4comment')

    s6_e1_damp = models.FloatField()
    s6_e1_Ramp = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s6e1comment')
    s6_e2_damp = models.FloatField()
    s6_e2_Ramp = models.FloatField()
    s6_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s6e2comment')
    s6_e3_damp = models.FloatField()
    s6_e3_Ramp = models.FloatField()
    s6_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s6e3comment')

    s7_e1_damp = models.FloatField()
    s7_e1_Ramp = models.FloatField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s7e1comment')
    s7_e2_damp = models.FloatField()
    s7_e2_Ramp = models.FloatField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s7e2comment')
    s7_e3_damp = models.FloatField()
    s7_e3_Ramp = models.FloatField()
    s7_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s7e3comment')
    s7_e4_damp = models.FloatField()
    s7_e4_Ramp = models.FloatField()
    s7_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s7e4comment')
    s7_e5_damp = models.FloatField()
    s7_e5_Ramp = models.FloatField()
    s7_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s7e5comment')

    s8_e1_bdisp = models.FloatField()
    s8_e1_slope = models.FloatField()
    s8_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s8e1comment')

    s9_e1_status = models.BooleanField(default=False)
    s9_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_ecg,on_delete=models.PROTECT, related_name='rme1s9e1comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class monitor_nibp_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='mn1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_nibp)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='mn1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='mn1caldev2',default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='mn1caldev3',default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_simp = models.IntegerField()
    s1_e1_nibpp = models.IntegerField()
    s1_e2_simp = models.IntegerField()
    s1_e2_nibpp = models.IntegerField()
    s1_e3_simp = models.IntegerField()
    s1_e3_nibpp = models.IntegerField()
    s1_e4_simp = models.IntegerField()
    s1_e4_nibpp = models.IntegerField()
    s1_e5_simp = models.IntegerField()
    s1_e5_nibpp = models.IntegerField()
    s1_e6_simp = models.IntegerField()
    s1_e6_nibpp = models.IntegerField()
    s1_e7_simp = models.IntegerField()
    s1_e7_nibpp = models.IntegerField()
    s1_e8_simp = models.IntegerField()
    s1_e8_nibpp = models.IntegerField()

    s2_e1_pr1 = models.IntegerField()
    s2_e1_pr2 = models.IntegerField()
    s2_e1_pr3 = models.IntegerField()
    s2_e2_pr1 = models.IntegerField()
    s2_e2_pr2 = models.IntegerField()
    s2_e2_pr3 = models.IntegerField()
    s2_e3_pr1 = models.IntegerField()
    s2_e3_pr2 = models.IntegerField()
    s2_e3_pr3 = models.IntegerField()
    s2_e4_pr1 = models.IntegerField()
    s2_e4_pr2 = models.IntegerField()
    s2_e4_pr3 = models.IntegerField()
    s2_e5_pr1 = models.IntegerField()
    s2_e5_pr2 = models.IntegerField()
    s2_e5_pr3 = models.IntegerField()
    s2_e6_pr1 = models.IntegerField()
    s2_e6_pr2 = models.IntegerField()
    s2_e6_pr3 = models.IntegerField()




    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_monitor_nibp_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rmn1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rmn1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_nibp)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='rmn1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rmn1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rmn1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_simp = models.IntegerField()
    s1_e1_nibpp = models.IntegerField()
    s1_e2_simp = models.IntegerField()
    s1_e2_nibpp = models.IntegerField()
    s1_e3_simp = models.IntegerField()
    s1_e3_nibpp = models.IntegerField()
    s1_e4_simp = models.IntegerField()
    s1_e4_nibpp = models.IntegerField()
    s1_e5_simp = models.IntegerField()
    s1_e5_nibpp = models.IntegerField()
    s1_e6_simp = models.IntegerField()
    s1_e6_nibpp = models.IntegerField()
    s1_e7_simp = models.IntegerField()
    s1_e7_nibpp = models.IntegerField()
    s1_e8_simp = models.IntegerField()
    s1_e8_nibpp = models.IntegerField()

    s2_e1_pr1 = models.IntegerField()
    s2_e1_pr2 = models.IntegerField()
    s2_e1_pr3 = models.IntegerField()
    s2_e2_pr1 = models.IntegerField()
    s2_e2_pr2 = models.IntegerField()
    s2_e2_pr3 = models.IntegerField()
    s2_e3_pr1 = models.IntegerField()
    s2_e3_pr2 = models.IntegerField()
    s2_e3_pr3 = models.IntegerField()
    s2_e4_pr1 = models.IntegerField()
    s2_e4_pr2 = models.IntegerField()
    s2_e4_pr3 = models.IntegerField()
    s2_e5_pr1 = models.IntegerField()
    s2_e5_pr2 = models.IntegerField()
    s2_e5_pr3 = models.IntegerField()
    s2_e6_pr1 = models.IntegerField()
    s2_e6_pr2 = models.IntegerField()
    s2_e6_pr3 = models.IntegerField()

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class aed_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='aed1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_aed)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='aed1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='aed1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT,related_name='aed1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s0e13comment')

    test_type = models.ForeignKey(acc.models.test_type,on_delete=models.CASCADE,related_name='aed1tt')

    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s1e1comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e5comment')
    s2_e6_lc = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e6comment')
    s2_e7_lc = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s2e7comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e5comment')
    s3_e6_lc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e6comment')
    s3_e7_lc = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s3e7comment')

    s4_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='aed1s4_t')

    s4_e1_lc1 = models.IntegerField(default=-1)
    s4_e1_lc2 = models.IntegerField(default=-1)
    s4_e1_lc3 = models.IntegerField(default=-1)
    s4_e1_lc4 = models.IntegerField(default=-1)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e1comment')
    s4_e2_lc1 = models.IntegerField(default=-1)
    s4_e2_lc2 = models.IntegerField(default=-1)
    s4_e2_lc3 = models.IntegerField(default=-1)
    s4_e2_lc4 = models.IntegerField(default=-1)
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e2comment')
    s4_e3_lc1 = models.IntegerField(default=-1)
    s4_e3_lc2 = models.IntegerField(default=-1)
    s4_e3_lc3 = models.IntegerField(default=-1)
    s4_e3_lc4 = models.IntegerField(default=-1)
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e3comment')
    s4_e4_lc1 = models.IntegerField(default=-1)
    s4_e4_lc2 = models.IntegerField(default=-1)
    s4_e4_lc3 = models.IntegerField(default=-1)
    s4_e4_lc4 = models.IntegerField(default=-1)
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e4comment')
    s4_e5_lc1 = models.IntegerField(default=-1)
    s4_e5_lc2 = models.IntegerField(default=-1)
    s4_e5_lc3 = models.IntegerField(default=-1)
    s4_e5_lc4 = models.IntegerField(default=-1)
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e5comment')
    s4_e6_lc1 = models.IntegerField(default=-1)
    s4_e6_lc2 = models.IntegerField(default=-1)
    s4_e6_lc3 = models.IntegerField(default=-1)
    s4_e6_lc4 = models.IntegerField(default=-1)
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e6comment')
    s4_e7_lc1 = models.IntegerField(default=-1)
    s4_e7_lc2 = models.IntegerField(default=-1)
    s4_e7_lc3 = models.IntegerField(default=-1)
    s4_e7_lc4 = models.IntegerField(default=-1)
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e7comment')
    s4_e8_lc1 = models.IntegerField(default=-1)
    s4_e8_lc2 = models.IntegerField(default=-1)
    s4_e8_lc3 = models.IntegerField(default=-1)
    s4_e8_lc4 = models.IntegerField(default=-1)
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e8comment')
    s4_e9_lc1 = models.IntegerField(default=-1)
    s4_e9_lc2 = models.IntegerField(default=-1)
    s4_e9_lc3 = models.IntegerField(default=-1)
    s4_e9_lc4 = models.IntegerField(default=-1)
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e9comment')
    s4_e10_lc1 = models.IntegerField(default=-1)
    s4_e10_lc2 = models.IntegerField(default=-1)
    s4_e10_lc3 = models.IntegerField(default=-1)
    s4_e10_lc4 = models.IntegerField(default=-1)
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s4e10comment')

    s5_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='aed1s5_t')

    s5_e1_lc1 = models.IntegerField(default=-1)
    s5_e1_lc2 = models.IntegerField(default=-1)
    s5_e1_lc3 = models.IntegerField(default=-1)
    s5_e1_lc4 = models.IntegerField(default=-1)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e1comment')
    s5_e2_lc1 = models.IntegerField(default=-1)
    s5_e2_lc2 = models.IntegerField(default=-1)
    s5_e2_lc3 = models.IntegerField(default=-1)
    s5_e2_lc4 = models.IntegerField(default=-1)
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e2comment')
    s5_e3_lc1 = models.IntegerField(default=-1)
    s5_e3_lc2 = models.IntegerField(default=-1)
    s5_e3_lc3 = models.IntegerField(default=-1)
    s5_e3_lc4 = models.IntegerField(default=-1)
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e3comment')
    s5_e4_lc1 = models.IntegerField(default=-1)
    s5_e4_lc2 = models.IntegerField(default=-1)
    s5_e4_lc3 = models.IntegerField(default=-1)
    s5_e4_lc4 = models.IntegerField(default=-1)
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e4comment')
    s5_e5_lc1 = models.IntegerField(default=-1)
    s5_e5_lc2 = models.IntegerField(default=-1)
    s5_e5_lc3 = models.IntegerField(default=-1)
    s5_e5_lc4 = models.IntegerField(default=-1)
    s5_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e5comment')
    s5_e6_lc1 = models.IntegerField(default=-1)
    s5_e6_lc2 = models.IntegerField(default=-1)
    s5_e6_lc3 = models.IntegerField(default=-1)
    s5_e6_lc4 = models.IntegerField(default=-1)
    s5_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e6comment')
    s5_e7_lc1 = models.IntegerField(default=-1)
    s5_e7_lc2 = models.IntegerField(default=-1)
    s5_e7_lc3 = models.IntegerField(default=-1)
    s5_e7_lc4 = models.IntegerField(default=-1)
    s5_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e7comment')
    s5_e8_lc1 = models.IntegerField(default=-1)
    s5_e8_lc2 = models.IntegerField(default=-1)
    s5_e8_lc3 = models.IntegerField(default=-1)
    s5_e8_lc4 = models.IntegerField(default=-1)
    s5_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e8comment')
    s5_e9_lc1 = models.IntegerField(default=-1)
    s5_e9_lc2 = models.IntegerField(default=-1)
    s5_e9_lc3 = models.IntegerField(default=-1)
    s5_e9_lc4 = models.IntegerField(default=-1)
    s5_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e9comment')
    s5_e10_lc1 = models.IntegerField(default=-1)
    s5_e10_lc2 = models.IntegerField(default=-1)
    s5_e10_lc3 = models.IntegerField(default=-1)
    s5_e10_lc4 = models.IntegerField(default=-1)
    s5_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s5e10comment')

    s6_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='aed1s6_t')

    s6_e1_lc1 = models.IntegerField()
    s6_e1_lc2 = models.IntegerField()
    s6_e1_lc3 = models.IntegerField()
    s6_e1_lc4 = models.IntegerField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='aed1s6e1comment')

    s11_e1_t = models.IntegerField()
    s11_e2_t = models.IntegerField()
    s11_e3_t = models.IntegerField()

    s12_e1_t = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='aed1s12e1comment')
    s13_e1_e = models.IntegerField()
    s13_e2_e = models.IntegerField()
    s13_e3_e = models.IntegerField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_aed_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='raed1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='raed1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_aed)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='raed1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='raed1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='raed1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()


    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT,related_name='raed1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                      related_name='raed1s0e13comment')

    test_type = models.ForeignKey(acc.models.test_type, on_delete=models.CASCADE,related_name='raed1tt')

    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s1e1comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e5comment')
    s2_e6_lc = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e6comment')
    s2_e7_lc = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s2e7comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e5comment')
    s3_e6_lc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e6comment')
    s3_e7_lc = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s3e7comment')

    s4_type = models.ForeignKey(acc.models.test_type2,on_delete=models.CASCADE,related_name='raed1s4_t')

    s4_e1_lc1 = models.IntegerField(default=-1)
    s4_e1_lc2 = models.IntegerField(default=-1)
    s4_e1_lc3 = models.IntegerField(default=-1)
    s4_e1_lc4 = models.IntegerField(default=-1)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e1comment')
    s4_e2_lc1 = models.IntegerField(default=-1)
    s4_e2_lc2 = models.IntegerField(default=-1)
    s4_e2_lc3 = models.IntegerField(default=-1)
    s4_e2_lc4 = models.IntegerField(default=-1)
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e2comment')
    s4_e3_lc1 = models.IntegerField(default=-1)
    s4_e3_lc2 = models.IntegerField(default=-1)
    s4_e3_lc3 = models.IntegerField(default=-1)
    s4_e3_lc4 = models.IntegerField(default=-1)
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e3comment')
    s4_e4_lc1 = models.IntegerField(default=-1)
    s4_e4_lc2 = models.IntegerField(default=-1)
    s4_e4_lc3 = models.IntegerField(default=-1)
    s4_e4_lc4 = models.IntegerField(default=-1)
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e4comment')
    s4_e5_lc1 = models.IntegerField(default=-1)
    s4_e5_lc2 = models.IntegerField(default=-1)
    s4_e5_lc3 = models.IntegerField(default=-1)
    s4_e5_lc4 = models.IntegerField(default=-1)
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e5comment')
    s4_e6_lc1 = models.IntegerField(default=-1)
    s4_e6_lc2 = models.IntegerField(default=-1)
    s4_e6_lc3 = models.IntegerField(default=-1)
    s4_e6_lc4 = models.IntegerField(default=-1)
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e6comment')
    s4_e7_lc1 = models.IntegerField(default=-1)
    s4_e7_lc2 = models.IntegerField(default=-1)
    s4_e7_lc3 = models.IntegerField(default=-1)
    s4_e7_lc4 = models.IntegerField(default=-1)
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e7comment')
    s4_e8_lc1 = models.IntegerField(default=-1)
    s4_e8_lc2 = models.IntegerField(default=-1)
    s4_e8_lc3 = models.IntegerField(default=-1)
    s4_e8_lc4 = models.IntegerField(default=-1)
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e8comment')
    s4_e9_lc1 = models.IntegerField(default=-1)
    s4_e9_lc2 = models.IntegerField(default=-1)
    s4_e9_lc3 = models.IntegerField(default=-1)
    s4_e9_lc4 = models.IntegerField(default=-1)
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e9comment')
    s4_e10_lc1 = models.IntegerField(default=-1)
    s4_e10_lc2 = models.IntegerField(default=-1)
    s4_e10_lc3 = models.IntegerField(default=-1)
    s4_e10_lc4 = models.IntegerField(default=-1)
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s4e10comment')

    s5_type = models.ForeignKey(acc.models.test_type2,on_delete=models.CASCADE,related_name='raed1s5_t')

    s5_e1_lc1 = models.IntegerField(default=-1)
    s5_e1_lc2 = models.IntegerField(default=-1)
    s5_e1_lc3 = models.IntegerField(default=-1)
    s5_e1_lc4 = models.IntegerField(default=-1)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e1comment')
    s5_e2_lc1 = models.IntegerField(default=-1)
    s5_e2_lc2 = models.IntegerField(default=-1)
    s5_e2_lc3 = models.IntegerField(default=-1)
    s5_e2_lc4 = models.IntegerField(default=-1)
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e2comment')
    s5_e3_lc1 = models.IntegerField(default=-1)
    s5_e3_lc2 = models.IntegerField(default=-1)
    s5_e3_lc3 = models.IntegerField(default=-1)
    s5_e3_lc4 = models.IntegerField(default=-1)
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e3comment')
    s5_e4_lc1 = models.IntegerField(default=-1)
    s5_e4_lc2 = models.IntegerField(default=-1)
    s5_e4_lc3 = models.IntegerField(default=-1)
    s5_e4_lc4 = models.IntegerField(default=-1)
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e4comment')
    s5_e5_lc1 = models.IntegerField(default=-1)
    s5_e5_lc2 = models.IntegerField(default=-1)
    s5_e5_lc3 = models.IntegerField(default=-1)
    s5_e5_lc4 = models.IntegerField(default=-1)
    s5_e5_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e5comment')
    s5_e6_lc1 = models.IntegerField(default=-1)
    s5_e6_lc2 = models.IntegerField(default=-1)
    s5_e6_lc3 = models.IntegerField(default=-1)
    s5_e6_lc4 = models.IntegerField(default=-1)
    s5_e6_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e6comment')
    s5_e7_lc1 = models.IntegerField(default=-1)
    s5_e7_lc2 = models.IntegerField(default=-1)
    s5_e7_lc3 = models.IntegerField(default=-1)
    s5_e7_lc4 = models.IntegerField(default=-1)
    s5_e7_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e7comment')
    s5_e8_lc1 = models.IntegerField(default=-1)
    s5_e8_lc2 = models.IntegerField(default=-1)
    s5_e8_lc3 = models.IntegerField(default=-1)
    s5_e8_lc4 = models.IntegerField(default=-1)
    s5_e8_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e8comment')
    s5_e9_lc1 = models.IntegerField(default=-1)
    s5_e9_lc2 = models.IntegerField(default=-1)
    s5_e9_lc3 = models.IntegerField(default=-1)
    s5_e9_lc4 = models.IntegerField(default=-1)
    s5_e9_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e9comment')
    s5_e10_lc1 = models.IntegerField(default=-1)
    s5_e10_lc2 = models.IntegerField(default=-1)
    s5_e10_lc3 = models.IntegerField(default=-1)
    s5_e10_lc4 = models.IntegerField(default=-1)
    s5_e10_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s5e10comment')

    s6_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='raed1s6_t')

    s6_e1_lc1 = models.IntegerField(default=-1)
    s6_e1_lc2 = models.IntegerField(default=-1)
    s6_e1_lc3 = models.IntegerField(default=-1)
    s6_e1_lc4 = models.IntegerField(default=-1)
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed,on_delete=models.PROTECT, related_name='raed1s6e1comment')

    s11_e1_t = models.IntegerField()
    s11_e2_t = models.IntegerField()
    s11_e3_t = models.IntegerField()

    s12_e1_t = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_aed, on_delete=models.PROTECT,
                                       related_name='raed1s12e1comment')

    s13_e1_e = models.IntegerField()
    s13_e2_e = models.IntegerField()
    s13_e3_e = models.IntegerField()# non shockable

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class monitor_safety_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='msa1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_safety)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='msa1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='msa1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety,on_delete=models.PROTECT,
                                      related_name='msa1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s0e22comment')


    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety,on_delete=models.PROTECT, related_name='msa1s1e1comment')
    s1_e2_res = models.IntegerField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s1e2comment')
    s1_e3_res = models.IntegerField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s1e3comment')
    s1_e4_res = models.IntegerField()
    s1_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s1e4comment')



    s2_e1_aplc = models.IntegerField()
    s2_e1_noaplc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety,on_delete=models.PROTECT, related_name='msa1s2e1comment')
    s2_e2_aplc = models.IntegerField()
    s2_e2_noaplc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s2e2comment')



    s3_e1_aplc = models.IntegerField()
    s3_e1_noaplc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e1comment')
    s3_e2_aplc = models.IntegerField()
    s3_e2_noaplc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e2comment')
    s3_e3_aplc = models.IntegerField()
    s3_e3_noaplc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e3comment')
    s3_e4_aplc = models.IntegerField()
    s3_e4_noaplc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e4comment')
    s3_e5_aplc = models.IntegerField()
    s3_e5_noaplc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e5comment')
    s3_e6_aplc = models.IntegerField()
    s3_e6_noaplc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s3e6comment')




    s4_e1_lc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety,on_delete=models.PROTECT,
                                      related_name='msa1s4e1comment')
    s4_e2_lc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e2comment')
    s4_e3_lc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e3comment')
    s4_e4_lc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e4comment')
    s4_e5_lc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e5comment')
    s4_e6_lc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e6comment')
    s4_e7_lc = models.IntegerField()
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e7comment')
    s4_e8_lc = models.IntegerField()
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e8comment')
    s4_e9_lc = models.IntegerField()
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e9comment')
    s4_e10_lc = models.IntegerField()
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e10comment')
    s4_e11_lc = models.IntegerField()
    s4_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e11comment')
    s4_e12_lc = models.IntegerField()
    s4_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e12comment')
    s4_e13_lc = models.IntegerField()
    s4_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e13comment')
    s4_e14_lc = models.IntegerField()
    s4_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e14comment')
    s4_e15_lc = models.IntegerField()
    s4_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e15comment')
    s4_e16_lc = models.IntegerField()
    s4_e16_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='msa1s4e16comment')
    s4_e17_lc = models.IntegerField()
    s4_e17_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e17comment')
    s4_e18_lc = models.IntegerField()
    s4_e18_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e18comment')
    s4_e19_lc = models.IntegerField()
    s4_e19_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e19comment')
    s4_e20_lc = models.IntegerField()
    s4_e20_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e20comment')
    s4_e21_lc = models.IntegerField()
    s4_e21_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e21comment')
    s4_e22_lc = models.IntegerField()
    s4_e22_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e22comment')
    s4_e23_lc = models.IntegerField()
    s4_e23_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e23comment')
    s4_e24_lc = models.IntegerField()
    s4_e24_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e24comment')
    s4_e25_lc = models.IntegerField()
    s4_e25_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e25comment')
    s4_e26_lc = models.IntegerField()
    s4_e26_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e26comment')
    s4_e27_lc = models.IntegerField()
    s4_e27_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e27comment')
    s4_e28_lc = models.IntegerField()
    s4_e28_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='msa1s4e28comment')




    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_monitor_safety_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rmsa1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rmsa1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_aed)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='rmsa1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rmsa1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT,related_name='rmsa1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s0e22comment')

    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s1e1comment')
    s1_e2_res = models.IntegerField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s1e2comment')
    s1_e3_res = models.IntegerField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s1e3comment')
    s1_e4_res = models.IntegerField()
    s1_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s1e4comment')

    s2_e1_aplc = models.IntegerField()
    s2_e1_noaplc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s2e1comment')
    s2_e2_aplc = models.IntegerField()
    s2_e2_noaplc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s2e2comment')

    s3_e1_aplc = models.IntegerField()
    s3_e1_noaplc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e1comment')
    s3_e2_aplc = models.IntegerField()
    s3_e2_noaplc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e2comment')
    s3_e3_aplc = models.IntegerField()
    s3_e3_noaplc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e3comment')
    s3_e4_aplc = models.IntegerField()
    s3_e4_noaplc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e4comment')
    s3_e5_aplc = models.IntegerField()
    s3_e5_noaplc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e5comment')
    s3_e6_aplc = models.IntegerField()
    s3_e6_noaplc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s3e6comment')

    s4_e1_lc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e1comment')
    s4_e2_lc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e2comment')
    s4_e3_lc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e3comment')
    s4_e4_lc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e4comment')
    s4_e5_lc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e5comment')
    s4_e6_lc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e6comment')
    s4_e7_lc = models.IntegerField()
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e7comment')
    s4_e8_lc = models.IntegerField()
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e8comment')
    s4_e9_lc = models.IntegerField()
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='rmsa1s4e9comment')
    s4_e10_lc = models.IntegerField()
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e10comment')
    s4_e11_lc = models.IntegerField()
    s4_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e11comment')
    s4_e12_lc = models.IntegerField()
    s4_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e12comment')
    s4_e13_lc = models.IntegerField()
    s4_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e13comment')
    s4_e14_lc = models.IntegerField()
    s4_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e14comment')
    s4_e15_lc = models.IntegerField()
    s4_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e15comment')
    s4_e16_lc = models.IntegerField()
    s4_e16_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e16comment')
    s4_e17_lc = models.IntegerField()
    s4_e17_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e17comment')
    s4_e18_lc = models.IntegerField()
    s4_e18_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e18comment')
    s4_e19_lc = models.IntegerField()
    s4_e19_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e19comment')
    s4_e20_lc = models.IntegerField()
    s4_e20_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e20comment')
    s4_e21_lc = models.IntegerField()
    s4_e21_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e21comment')
    s4_e22_lc = models.IntegerField()
    s4_e22_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e22comment')
    s4_e23_lc = models.IntegerField()
    s4_e23_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e23comment')
    s4_e24_lc = models.IntegerField()
    s4_e24_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e24comment')
    s4_e25_lc = models.IntegerField()
    s4_e25_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e25comment')
    s4_e26_lc = models.IntegerField()
    s4_e26_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e26comment')
    s4_e27_lc = models.IntegerField()
    s4_e27_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e27comment')
    s4_e28_lc = models.IntegerField()
    s4_e28_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='rmsa1s4e28comment')

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class anesthesia_machine_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='am1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_anesthesia_machine)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='am1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='am1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='am1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='am1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT,related_name='am1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e23comment')
    s0_e24_status = models.BooleanField(default=False)
    s0_e24_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e24comment')
    s0_e25_status = models.BooleanField(default=False)
    s0_e25_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e25comment')
    s0_e26_status = models.BooleanField(default=False)
    s0_e26_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e26comment')
    s0_e27_status = models.BooleanField(default=False)
    s0_e27_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e27comment')
    s0_e28_status = models.BooleanField(default=False)
    s0_e28_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e28comment')
    s0_e29_status = models.BooleanField(default=False)
    s0_e29_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e29comment')
    s0_e30_status = models.BooleanField(default=False)
    s0_e30_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e30comment')
    s0_e31_status = models.BooleanField(default=False)
    s0_e31_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='am1s0e31comment')


    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s2e5comment')



    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s3e5comment')


    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT,
                                      related_name='am1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='am1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine,on_delete=models.PROTECT, related_name='am1s5e1comment')

    s6_e1_rff = models.IntegerField()
    s6_e1_ffr = models.IntegerField()

    s7_e1_si1 = models.IntegerField()
    s7_e1_si2 = models.IntegerField()
    s7_e1_si3 = models.IntegerField()
    s7_e1_si4 = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    s9_e1 = models.IntegerField()

    s10_e1 = models.IntegerField()

    s11_e1_status = models.BooleanField(default=False)


    s12_e1 = models.IntegerField()
    s12_e2 = models.IntegerField()
    s12_e3 = models.IntegerField()

    s13_e1_ro2f = models.IntegerField()
    s13_e1_ro2n20f = models.IntegerField()
    s13_e2_ro2f = models.IntegerField()
    s13_e2_ro2n20f = models.IntegerField()
    s13_e3_o2p = models.IntegerField()
    s13_e3_ro2d = models.IntegerField()
    s13_e3_ro2c = models.IntegerField()

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()

    s15_e1 = models.IntegerField()
    s15_e2 = models.IntegerField()
    s15_e3 = models.IntegerField()

    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()

    s17_e1 = models.IntegerField()
    s17_e2 = models.IntegerField()
    s17_e3 = models.IntegerField()
    s17_e4 = models.IntegerField()
    s17_e5 = models.IntegerField()
    s17_e6 = models.IntegerField()

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_anesthesia_machine_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='ram1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='ram1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_aed)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ram1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ram1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ram1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ram1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e23comment')
    s0_e24_status = models.BooleanField(default=False)
    s0_e24_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e24comment')
    s0_e25_status = models.BooleanField(default=False)
    s0_e25_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e25comment')
    s0_e26_status = models.BooleanField(default=False)
    s0_e26_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e26comment')
    s0_e27_status = models.BooleanField(default=False)
    s0_e27_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e27comment')
    s0_e28_status = models.BooleanField(default=False)
    s0_e28_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e28comment')
    s0_e29_status = models.BooleanField(default=False)
    s0_e29_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e29comment')
    s0_e30_status = models.BooleanField(default=False)
    s0_e30_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e30comment')
    s0_e31_status = models.BooleanField(default=False)
    s0_e31_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                       related_name='ram1s0e31comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s2e5comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s3e5comment')

    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s5e1comment')

    s6_e1_rff = models.IntegerField()
    s6_e1_ffr = models.IntegerField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_anesthesia_machine, on_delete=models.PROTECT,
                                      related_name='ram1s6e1comment')

    s7_e1_si1 = models.IntegerField()
    s7_e1_si2 = models.IntegerField()
    s7_e1_si3 = models.IntegerField()
    s7_e1_si4 = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    s9_e1 = models.IntegerField()

    s10_e1 = models.IntegerField()

    s11_e1_status = models.BooleanField(default=False)

    s12_e1 = models.IntegerField()
    s12_e2 = models.IntegerField()
    s12_e3 = models.IntegerField()

    s13_e1_ro2f = models.IntegerField()
    s13_e1_ro2n20f = models.IntegerField()
    s13_e2_ro2f = models.IntegerField()
    s13_e2_ro2n20f = models.IntegerField()
    s13_e3_ro2d = models.IntegerField()
    s13_e3_ro2c = models.IntegerField()

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()

    s15_e1 = models.IntegerField()
    s15_e2 = models.IntegerField()
    s15_e3 = models.IntegerField()

    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()

    s17_e1 = models.IntegerField()
    s17_e2 = models.IntegerField()
    s17_e3 = models.IntegerField()
    s17_e4 = models.IntegerField()
    s17_e5 = models.IntegerField()
    s17_e6 = models.IntegerField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class defibrilator_1(models.Model):
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE, related_name='df1licence')
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_defibrilator)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='df1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='df1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='df1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='df1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s0e22comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s1e1comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e5comment')
    s2_e6_lc = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e6comment')
    s2_e7_lc = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s2e7comment')


    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e5comment')
    s3_e6_lc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e6comment')
    s3_e7_lc = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s3e7comment')

    s4_e1_lc1 = models.IntegerField()
    s4_e1_lc2 = models.IntegerField()
    s4_e1_lc3 = models.IntegerField()
    s4_e1_lc4 = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e1comment')
    s4_e2_lc1 = models.IntegerField()
    s4_e2_lc2 = models.IntegerField()
    s4_e2_lc3 = models.IntegerField()
    s4_e2_lc4 = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e2comment')
    s4_e3_lc1 = models.IntegerField()
    s4_e3_lc2 = models.IntegerField()
    s4_e3_lc3 = models.IntegerField()
    s4_e3_lc4 = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e3comment')
    s4_e4_lc1 = models.IntegerField()
    s4_e4_lc2 = models.IntegerField()
    s4_e4_lc3 = models.IntegerField()
    s4_e4_lc4 = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e4comment')
    s4_e5_lc1 = models.IntegerField()
    s4_e5_lc2 = models.IntegerField()
    s4_e5_lc3 = models.IntegerField()
    s4_e5_lc4 = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e5comment')
    s4_e6_lc1 = models.IntegerField()
    s4_e6_lc2 = models.IntegerField()
    s4_e6_lc3 = models.IntegerField()
    s4_e6_lc4 = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e6comment')
    s4_e7_lc1 = models.IntegerField()
    s4_e7_lc2 = models.IntegerField()
    s4_e7_lc3 = models.IntegerField()
    s4_e7_lc4 = models.IntegerField()
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e7comment')
    s4_e8_lc1 = models.IntegerField()
    s4_e8_lc2 = models.IntegerField()
    s4_e8_lc3 = models.IntegerField()
    s4_e8_lc4 = models.IntegerField()
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e8comment')
    s4_e9_lc1 = models.IntegerField()
    s4_e9_lc2 = models.IntegerField()
    s4_e9_lc3 = models.IntegerField()
    s4_e9_lc4 = models.IntegerField()
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s4e9comment')
    s4_e10_lc1 = models.IntegerField()
    s4_e10_lc2 = models.IntegerField()
    s4_e10_lc3 = models.IntegerField()
    s4_e10_lc4 = models.IntegerField()
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s4e10comment')

    s5_e1_lc1 = models.IntegerField()
    s5_e1_lc2 = models.IntegerField()
    s5_e1_lc3 = models.IntegerField()
    s5_e1_lc4 = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e1comment')
    s5_e2_lc1 = models.IntegerField()
    s5_e2_lc2 = models.IntegerField()
    s5_e2_lc3 = models.IntegerField()
    s5_e2_lc4 = models.IntegerField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e2comment')
    s5_e3_lc1 = models.IntegerField()
    s5_e3_lc2 = models.IntegerField()
    s5_e3_lc3 = models.IntegerField()
    s5_e3_lc4 = models.IntegerField()
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e3comment')
    s5_e4_lc1 = models.IntegerField()
    s5_e4_lc2 = models.IntegerField()
    s5_e4_lc3 = models.IntegerField()
    s5_e4_lc4 = models.IntegerField()
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e4comment')
    s5_e5_lc1 = models.IntegerField()
    s5_e5_lc2 = models.IntegerField()
    s5_e5_lc3 = models.IntegerField()
    s5_e5_lc4 = models.IntegerField()
    s5_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e5comment')
    s5_e6_lc1 = models.IntegerField()
    s5_e6_lc2 = models.IntegerField()
    s5_e6_lc3 = models.IntegerField()
    s5_e6_lc4 = models.IntegerField()
    s5_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e6comment')
    s5_e7_lc1 = models.IntegerField()
    s5_e7_lc2 = models.IntegerField()
    s5_e7_lc3 = models.IntegerField()
    s5_e7_lc4 = models.IntegerField()
    s5_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e7comment')
    s5_e8_lc1 = models.IntegerField()
    s5_e8_lc2 = models.IntegerField()
    s5_e8_lc3 = models.IntegerField()
    s5_e8_lc4 = models.IntegerField()
    s5_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e8comment')
    s5_e9_lc1 = models.IntegerField()
    s5_e9_lc2 = models.IntegerField()
    s5_e9_lc3 = models.IntegerField()
    s5_e9_lc4 = models.IntegerField()
    s5_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s5e9comment')
    s5_e10_lc1 = models.IntegerField()
    s5_e10_lc2 = models.IntegerField()
    s5_e10_lc3 = models.IntegerField()
    s5_e10_lc4 = models.IntegerField()
    s5_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s5e10comment')

    s6_e1_lc1 = models.IntegerField()
    s6_e1_lc2 = models.IntegerField()
    s6_e1_lc3 = models.IntegerField()
    s6_e1_lc4 = models.IntegerField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s6e1comment')



    s7a_e1_es = models.IntegerField()
    s7a_e1_em = models.IntegerField()
    s7a_e1_ec = models.IntegerField()
    s7a_e1_v = models.IntegerField()
    s7a_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s7ae1comment')

    s7a_e2_es = models.IntegerField()
    s7a_e2_em = models.IntegerField()
    s7a_e2_ec = models.IntegerField()
    s7a_e2_v = models.IntegerField()
    s7a_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s7ae2comment')
    s7a_e3_es = models.IntegerField()
    s7a_e3_em = models.IntegerField()
    s7a_e3_ec = models.IntegerField()
    s7a_e3_v = models.IntegerField()
    s7a_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s7ae3comment')

    s7b_e1_es = models.IntegerField()
    s7b_e1_em = models.IntegerField()
    s7b_e1_ec = models.IntegerField()
    s7b_e1_v = models.IntegerField()
    s7b_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7be1comment')

    s7b_e2_es = models.IntegerField()
    s7b_e2_em = models.IntegerField()
    s7b_e2_ec = models.IntegerField()
    s7b_e2_v = models.IntegerField()
    s7b_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7be2comment')
    s7b_e3_es = models.IntegerField()
    s7b_e3_em = models.IntegerField()
    s7b_e3_ec = models.IntegerField()
    s7b_e3_v = models.IntegerField()
    s7b_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7be3comment')
    s7c_e1_es = models.IntegerField()
    s7c_e1_em = models.IntegerField()
    s7c_e1_ec = models.IntegerField()
    s7c_e1_v = models.IntegerField()
    s7c_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7ce1comment')

    s7c_e2_es = models.IntegerField()
    s7c_e2_em = models.IntegerField()
    s7c_e2_ec = models.IntegerField()
    s7c_e2_v = models.IntegerField()
    s7c_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7ce2comment')
    s7c_e3_es = models.IntegerField()
    s7c_e3_em = models.IntegerField()
    s7c_e3_ec = models.IntegerField()
    s7c_e3_v = models.IntegerField()
    s7c_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7ce3comment')

    s7d_e1_en = models.IntegerField()
    s7d_e1_es = models.IntegerField()
    s7d_e1_ec = models.IntegerField()
    s7d_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s7de1comment')

    s8_e1_en = models.IntegerField()
    s8_e1_em1 = models.IntegerField()
    s8_e1_em2 = models.IntegerField()
    s8_e1_ec = models.IntegerField()
    s8_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s8e1comment')
    s9_e1_en = models.IntegerField()
    s9_e1_t1 = models.IntegerField()
    s9_e1_tc = models.IntegerField()
    s9_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s9e1comment')
    s10_e1_ct = models.IntegerField()
    s10_e1_en = models.IntegerField()
    s10_e1_enl = models.IntegerField()
    s10_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='df1s10e1comment')
    s10_e2_ct = models.IntegerField()
    s10_e2_en = models.IntegerField()
    s10_e2_enl = models.IntegerField()
    s10_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e2comment')
    s10_e3_ct = models.IntegerField()
    s10_e3_en = models.IntegerField()
    s10_e3_enl = models.IntegerField()
    s10_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e3comment')
    s10_e4_ct = models.IntegerField()
    s10_e4_en = models.IntegerField()
    s10_e4_enl = models.IntegerField()
    s10_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e4comment')
    s10_e5_ct = models.IntegerField()
    s10_e5_en = models.IntegerField()
    s10_e5_enl = models.IntegerField()
    s10_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e5comment')
    s10_e6_ct = models.IntegerField()
    s10_e6_en = models.IntegerField()
    s10_e6_enl = models.IntegerField()
    s10_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e6comment')
    s10_e7_ct = models.IntegerField()
    s10_e7_en = models.IntegerField()
    s10_e7_enl = models.IntegerField()
    s10_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e7comment')
    s10_e8_ct = models.IntegerField()
    s10_e8_en = models.IntegerField()
    s10_e8_enl = models.IntegerField()
    s10_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e8comment')
    s10_e9_ct = models.IntegerField()
    s10_e9_en = models.IntegerField()
    s10_e9_enl = models.IntegerField()
    s10_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e9comment')
    s10_e10_ct = models.IntegerField()
    s10_e10_en = models.IntegerField()
    s10_e10_enl = models.IntegerField()
    s10_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s10e10comment')

    s11_e1_en = models.IntegerField()
    s11_e1_t = models.IntegerField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                        related_name='df1s11e1comment')


    s12_e1_en = models.IntegerField()
    s12_e1_dc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s12e1comment')
    s12_e2_en = models.IntegerField()
    s12_e2_cc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s12e2comment')
    s12_e3_en = models.IntegerField()
    s12_e3_cc = models.IntegerField()
    s12_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='df1s12e3comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_defibrilator_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rdf1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rdf1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_defibrilator)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rdf1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rdf1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rdf1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rdf1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s0e22comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s1e1comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e5comment')
    s2_e6_lc = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e6comment')
    s2_e7_lc = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s2e7comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e5comment')
    s3_e6_lc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e6comment')
    s3_e7_lc = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s3e7comment')

    s4_e1_lc1 = models.IntegerField()
    s4_e1_lc2 = models.IntegerField()
    s4_e1_lc3 = models.IntegerField()
    s4_e1_lc4 = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e1comment')
    s4_e2_lc1 = models.IntegerField()
    s4_e2_lc2 = models.IntegerField()
    s4_e2_lc3 = models.IntegerField()
    s4_e2_lc4 = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e2comment')
    s4_e3_lc1 = models.IntegerField()
    s4_e3_lc2 = models.IntegerField()
    s4_e3_lc3 = models.IntegerField()
    s4_e3_lc4 = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e3comment')
    s4_e4_lc1 = models.IntegerField()
    s4_e4_lc2 = models.IntegerField()
    s4_e4_lc3 = models.IntegerField()
    s4_e4_lc4 = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e4comment')
    s4_e5_lc1 = models.IntegerField()
    s4_e5_lc2 = models.IntegerField()
    s4_e5_lc3 = models.IntegerField()
    s4_e5_lc4 = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e5comment')
    s4_e6_lc1 = models.IntegerField()
    s4_e6_lc2 = models.IntegerField()
    s4_e6_lc3 = models.IntegerField()
    s4_e6_lc4 = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e6comment')
    s4_e7_lc1 = models.IntegerField()
    s4_e7_lc2 = models.IntegerField()
    s4_e7_lc3 = models.IntegerField()
    s4_e7_lc4 = models.IntegerField()
    s4_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e7comment')
    s4_e8_lc1 = models.IntegerField()
    s4_e8_lc2 = models.IntegerField()
    s4_e8_lc3 = models.IntegerField()
    s4_e8_lc4 = models.IntegerField()
    s4_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e8comment')
    s4_e9_lc1 = models.IntegerField()
    s4_e9_lc2 = models.IntegerField()
    s4_e9_lc3 = models.IntegerField()
    s4_e9_lc4 = models.IntegerField()
    s4_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s4e9comment')
    s4_e10_lc1 = models.IntegerField()
    s4_e10_lc2 = models.IntegerField()
    s4_e10_lc3 = models.IntegerField()
    s4_e10_lc4 = models.IntegerField()
    s4_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s4e10comment')

    s5_e1_lc1 = models.IntegerField()
    s5_e1_lc2 = models.IntegerField()
    s5_e1_lc3 = models.IntegerField()
    s5_e1_lc4 = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e1comment')
    s5_e2_lc1 = models.IntegerField()
    s5_e2_lc2 = models.IntegerField()
    s5_e2_lc3 = models.IntegerField()
    s5_e2_lc4 = models.IntegerField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e2comment')
    s5_e3_lc1 = models.IntegerField()
    s5_e3_lc2 = models.IntegerField()
    s5_e3_lc3 = models.IntegerField()
    s5_e3_lc4 = models.IntegerField()
    s5_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e3comment')
    s5_e4_lc1 = models.IntegerField()
    s5_e4_lc2 = models.IntegerField()
    s5_e4_lc3 = models.IntegerField()
    s5_e4_lc4 = models.IntegerField()
    s5_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e4comment')
    s5_e5_lc1 = models.IntegerField()
    s5_e5_lc2 = models.IntegerField()
    s5_e5_lc3 = models.IntegerField()
    s5_e5_lc4 = models.IntegerField()
    s5_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e5comment')
    s5_e6_lc1 = models.IntegerField()
    s5_e6_lc2 = models.IntegerField()
    s5_e6_lc3 = models.IntegerField()
    s5_e6_lc4 = models.IntegerField()
    s5_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e6comment')
    s5_e7_lc1 = models.IntegerField()
    s5_e7_lc2 = models.IntegerField()
    s5_e7_lc3 = models.IntegerField()
    s5_e7_lc4 = models.IntegerField()
    s5_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e7comment')
    s5_e8_lc1 = models.IntegerField()
    s5_e8_lc2 = models.IntegerField()
    s5_e8_lc3 = models.IntegerField()
    s5_e8_lc4 = models.IntegerField()
    s5_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e8comment')
    s5_e9_lc1 = models.IntegerField()
    s5_e9_lc2 = models.IntegerField()
    s5_e9_lc3 = models.IntegerField()
    s5_e9_lc4 = models.IntegerField()
    s5_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s5e9comment')
    s5_e10_lc1 = models.IntegerField()
    s5_e10_lc2 = models.IntegerField()
    s5_e10_lc3 = models.IntegerField()
    s5_e10_lc4 = models.IntegerField()
    s5_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s5e10comment')

    s6_e1_lc1 = models.IntegerField()
    s6_e1_lc2 = models.IntegerField()
    s6_e1_lc3 = models.IntegerField()
    s6_e1_lc4 = models.IntegerField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s6e1comment')

    s7a_e1_es = models.IntegerField()
    s7a_e1_em = models.IntegerField()
    s7a_e1_ec = models.IntegerField()
    s7a_e1_v = models.IntegerField()
    s7a_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ae1comment')

    s7a_e2_es = models.IntegerField()
    s7a_e2_em = models.IntegerField()
    s7a_e2_ec = models.IntegerField()
    s7a_e2_v = models.IntegerField()
    s7a_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ae2comment')
    s7a_e3_es = models.IntegerField()
    s7a_e3_em = models.IntegerField()
    s7a_e3_ec = models.IntegerField()
    s7a_e3_v = models.IntegerField()
    s7a_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ae3comment')

    s7b_e1_es = models.IntegerField()
    s7b_e1_em = models.IntegerField()
    s7b_e1_ec = models.IntegerField()
    s7b_e1_v = models.IntegerField()
    s7b_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7be1comment')

    s7b_e2_es = models.IntegerField()
    s7b_e2_em = models.IntegerField()
    s7b_e2_ec = models.IntegerField()
    s7b_e2_v = models.IntegerField()
    s7b_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7be2comment')
    s7b_e3_es = models.IntegerField()
    s7b_e3_em = models.IntegerField()
    s7b_e3_ec = models.IntegerField()
    s7b_e3_v = models.IntegerField()
    s7b_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7be3comment')
    s7c_e1_es = models.IntegerField()
    s7c_e1_em = models.IntegerField()
    s7c_e1_ec = models.IntegerField()
    s7c_e1_v = models.IntegerField()
    s7c_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ce1comment')

    s7c_e2_es = models.IntegerField()
    s7c_e2_em = models.IntegerField()
    s7c_e2_ec = models.IntegerField()
    s7c_e2_v = models.IntegerField()
    s7c_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ce2comment')
    s7c_e3_es = models.IntegerField()
    s7c_e3_em = models.IntegerField()
    s7c_e3_ec = models.IntegerField()
    s7c_e3_v = models.IntegerField()
    s7c_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7ce3comment')

    s7d_e1_en = models.IntegerField()
    s7d_e1_es = models.IntegerField()
    s7d_e1_ec = models.IntegerField()
    s7d_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s7de1comment')

    s8_e1_en = models.IntegerField()
    s8_e1_em1 = models.IntegerField()
    s8_e1_em2 = models.IntegerField()
    s8_e1_ec = models.IntegerField()
    s8_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s8e1comment')
    s9_e1_en = models.IntegerField()
    s9_e1_t1 = models.IntegerField()
    s9_e1_tc = models.IntegerField()
    s9_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                      related_name='rdf1s9e1comment')
    s10_e1_ct = models.IntegerField()
    s10_e1_en = models.IntegerField()
    s10_e1_enl = models.IntegerField()
    s10_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e1comment')
    s10_e2_ct = models.IntegerField()
    s10_e2_en = models.IntegerField()
    s10_e2_enl = models.IntegerField()
    s10_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e2comment')
    s10_e3_ct = models.IntegerField()
    s10_e3_en = models.IntegerField()
    s10_e3_enl = models.IntegerField()
    s10_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e3comment')
    s10_e4_ct = models.IntegerField()
    s10_e4_en = models.IntegerField()
    s10_e4_enl = models.IntegerField()
    s10_e4_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e4comment')
    s10_e5_ct = models.IntegerField()
    s10_e5_en = models.IntegerField()
    s10_e5_enl = models.IntegerField()
    s10_e5_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e5comment')
    s10_e6_ct = models.IntegerField()
    s10_e6_en = models.IntegerField()
    s10_e6_enl = models.IntegerField()
    s10_e6_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e6comment')
    s10_e7_ct = models.IntegerField()
    s10_e7_en = models.IntegerField()
    s10_e7_enl = models.IntegerField()
    s10_e7_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e7comment')
    s10_e8_ct = models.IntegerField()
    s10_e8_en = models.IntegerField()
    s10_e8_enl = models.IntegerField()
    s10_e8_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e8comment')
    s10_e9_ct = models.IntegerField()
    s10_e9_en = models.IntegerField()
    s10_e9_enl = models.IntegerField()
    s10_e9_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s10e9comment')
    s10_e10_ct = models.IntegerField()
    s10_e10_en = models.IntegerField()
    s10_e10_enl = models.IntegerField()
    s10_e10_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                        related_name='rdf1s10e10comment')

    s11_e1_en = models.IntegerField()
    s11_e1_t = models.IntegerField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s11e1comment')

    s12_e1_en = models.IntegerField()
    s12_e1_dc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s12e1comment')
    s12_e2_en = models.IntegerField()
    s12_e2_cc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s12e2comment')
    s12_e3_en = models.IntegerField()
    s12_e3_cc = models.IntegerField()
    s12_e3_comment = models.ForeignKey(acc.models.quantitive_comment_defibrilator, on_delete=models.PROTECT,
                                       related_name='rdf1s12e3comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class ecg_1(models.Model):
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE, related_name='e1licence')
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_ecg)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='e1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='e1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='e1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='e1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()


    s1_e1_damp = models.FloatField()
    s1_e1_Ramp = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s1e1comment')
    s1_e2_damp = models.FloatField()
    s1_e2_Ramp = models.FloatField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s1e2comment')
    s1_e3_damp = models.FloatField()
    s1_e3_Ramp = models.FloatField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s1e3comment')


    s2_e1_nspeak = models.IntegerField()
    s2_e2_nspeak = models.IntegerField()
    s2_e3_nspeak = models.IntegerField()
    s2_e4_nspeak = models.IntegerField()
    s2_e5_nspeak = models.IntegerField()
    s2_e6_nspeak = models.IntegerField()

    s3_e1_mr = models.FloatField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg,on_delete=models.PROTECT,
                                      related_name='e1s3e1comment')

    s4_e1_mr = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e1comment')
    s4_e2_mr = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e2comment')
    s4_e3_mr = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e3comment')
    s4_e4_mr = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e4comment')
    s4_e5_mr = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e5comment')
    s4_e6_mr = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s4e6comment')

    s5_e1_mr = models.IntegerField()
    s5_e2_mr = models.IntegerField()
    s5_e3_mr = models.IntegerField()
    s5_e4_mr = models.IntegerField()
    s5_e5_mr = models.IntegerField()
    s5_e6_mr = models.IntegerField()
    s5_e7_mr = models.IntegerField()
    s5_e8_mr = models.IntegerField()
    s5_e9_mr = models.IntegerField()
    s5_e10_mr = models.IntegerField()
    s5_e11_mr = models.IntegerField()
    s5_e12_mr = models.IntegerField()

    s6_e1_ramp = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s6e1comment')
    s6_e2_ramp = models.FloatField()
    s6_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s6e2comment')
    s6_e3_ramp = models.FloatField()
    s6_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s6e3comment')

    s7_e1_status = models.BooleanField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e1comment')
    s7_e2_status = models.BooleanField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e2comment')
    s7_e3_status = models.BooleanField()
    s7_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e3comment')
    s7_e4_status = models.BooleanField()
    s7_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e4comment')
    s7_e5_status = models.BooleanField()
    s7_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e5comment')
    s7_e6_status = models.BooleanField()
    s7_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e6comment')
    s7_e7_status = models.BooleanField()
    s7_e7_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e7comment')
    s7_e8_status = models.BooleanField()
    s7_e8_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s7e8comment')


    s11_e1_acc = models.ForeignKey(acc.models.accessory,on_delete=models.PROTECT,related_name='e1s11e1accessory',default=1)   #N/A
    s11_e1_status = models.BooleanField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='e1s11e1comment')

    s11_e2_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='e1s11e2accessory',
                                   default=1)  # N/A
    s11_e2_status = models.BooleanField()
    s11_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s11e2comment')

    s11_e3_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='e1s11e3accessory',
                                   default=1)  # N/A
    s11_e3_status = models.BooleanField()
    s11_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s11e3comment')

    s11_e4_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='e1s11e4accessory',
                                   default=1)  # N/A
    s11_e4_status = models.BooleanField()
    s11_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s11e4comment')

    s11_e5_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='e1s11e5accessory',
                                   default=1)  # N/A
    s11_e5_status = models.BooleanField()
    s11_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s11e5comment')


    s12_e1_status = models.BooleanField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s12e1comment')
    s12_e2_status = models.BooleanField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s12e2comment')
    s12_e3_status = models.BooleanField()
    s12_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s12e3comment')
    s12_e4_status = models.BooleanField()
    s12_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s12e4comment')

    s13_e1_va = models.FloatField()
    s13_e1_watt = models.FloatField()
    s13_e1_v = models.FloatField()
    s13_e1_a = models.FloatField()

    s14_e1_type = models.BooleanField()
    s14_e1_er = models.FloatField()
    s14_e1_pe = models.FloatField()
    s14_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='e1s14e1comment')

    s15_e1_aplc = models.IntegerField()
    s15_e1_noaplc = models.IntegerField()
    s15_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='e1s15e1comment')
    s15_e2_aplc = models.IntegerField()
    s15_e2_noaplc = models.IntegerField()
    s15_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='e1s15e2comment')

    s16_e1_aplc = models.IntegerField()
    s16_e1_noaplc = models.IntegerField()
    s16_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='e1s16e1comment')
    s16_e2_aplc = models.IntegerField()
    s16_e2_noaplc = models.IntegerField()
    s16_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='e1s16e2comment')

    s17_e1_plc = models.IntegerField()
    s17_e1_pe = models.IntegerField()
    s17_e2_plc = models.IntegerField()
    s17_e2_pe = models.IntegerField()
    s17_e3_plc = models.IntegerField()
    s17_e3_pe = models.IntegerField()
    s17_e4_plc = models.IntegerField()
    s17_e4_pe = models.IntegerField()
    s17_e5_plc = models.IntegerField()
    s17_e5_pe = models.IntegerField()
    s17_e6_plc = models.IntegerField()
    s17_e6_pe = models.IntegerField()
    s17_e7_plc = models.IntegerField()
    s17_e7_pe = models.IntegerField()
    s17_e8_plc = models.IntegerField()
    s17_e8_pe = models.IntegerField()
    s17_e9_plc = models.IntegerField()
    s17_e9_pe = models.IntegerField()
    s17_e10_plc = models.IntegerField()
    s17_e10_pe = models.IntegerField()
    s17_e11_plc = models.IntegerField()
    s17_e11_pe = models.IntegerField()
    s17_e12_plc = models.IntegerField()
    s17_e12_pe = models.IntegerField()

    s18_e1_pac = models.IntegerField()
    s18_e1_pe = models.IntegerField()
    s18_e2_pac = models.IntegerField()
    s18_e2_pe = models.IntegerField()
    s18_e3_pac = models.IntegerField()
    s18_e3_pe = models.IntegerField()
    s18_e4_pac = models.IntegerField()
    s18_e4_pe = models.IntegerField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_ecg_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='re1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='re1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_defibrilator)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='re1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='re1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='re1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='re1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()


    s1_e1_damp = models.FloatField()
    s1_e1_Ramp = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s1e1comment')
    s1_e2_damp = models.FloatField()
    s1_e2_Ramp = models.FloatField()
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s1e2comment')
    s1_e3_damp = models.FloatField()
    s1_e3_Ramp = models.FloatField()
    s1_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s1e3comment')


    s2_e1_nspeak = models.IntegerField()
    s2_e2_nspeak = models.IntegerField()
    s2_e3_nspeak = models.IntegerField()
    s2_e4_nspeak = models.IntegerField()
    s2_e5_nspeak = models.IntegerField()
    s2_e6_nspeak = models.IntegerField()

    s3_e1_mr = models.FloatField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg,on_delete=models.PROTECT,
                                      related_name='re1s3e1comment')

    s4_e1_mr = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e1comment')
    s4_e2_mr = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e2comment')
    s4_e3_mr = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e3comment')
    s4_e4_mr = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e4comment')
    s4_e5_mr = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e5comment')
    s4_e6_mr = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s4e6comment')

    s5_e1_mr = models.IntegerField()
    s5_e2_mr = models.IntegerField()
    s5_e3_mr = models.IntegerField()
    s5_e4_mr = models.IntegerField()
    s5_e5_mr = models.IntegerField()
    s5_e6_mr = models.IntegerField()
    s5_e7_mr = models.IntegerField()
    s5_e8_mr = models.IntegerField()
    s5_e9_mr = models.IntegerField()
    s5_e10_mr = models.IntegerField()
    s5_e11_mr = models.IntegerField()
    s5_e12_mr = models.IntegerField()

    s6_e1_ramp = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s6e1comment')
    s6_e2_ramp = models.FloatField()
    s6_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s6e2comment')
    s6_e3_ramp = models.FloatField()
    s6_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s6e3comment')

    s7_e1_status = models.BooleanField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e1comment')
    s7_e2_status = models.BooleanField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e2comment')

    s7_e3_status = models.BooleanField()
    s7_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e3comment')

    s7_e4_status = models.BooleanField()
    s7_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e4comment')

    s7_e5_status = models.BooleanField()
    s7_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e5comment')

    s7_e6_status = models.BooleanField()
    s7_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e6comment')

    s7_e7_status = models.BooleanField()
    s7_e7_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e7comment')

    s7_e8_status = models.BooleanField()
    s7_e8_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s7e8comment')


    s11_e1_acc = models.ForeignKey(acc.models.accessory,on_delete=models.PROTECT,related_name='re1s11e1accessory',default=1)   #N/A
    s11_e1_status = models.BooleanField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                      related_name='re1s11e1comment')

    s11_e2_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='re1s11e2accessory',
                                   default=1)  # N/A
    s11_e2_status = models.BooleanField()
    s11_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s11e2comment')

    s11_e3_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='re1s11e3accessory',
                                   default=1)  # N/A
    s11_e3_status = models.BooleanField()
    s11_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s11e3comment')

    s11_e4_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='re1s11e4accessory',
                                   default=1)  # N/A
    s11_e4_status = models.BooleanField()
    s11_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s11e4comment')

    s11_e5_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='re1s11e5accessory',
                                   default=1)  # N/A
    s11_e5_status = models.BooleanField()
    s11_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s11e5comment')


    s12_e1_status = models.BooleanField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s12e1comment')
    s12_e2_status = models.BooleanField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s12e2comment')
    s12_e3_status = models.BooleanField()
    s12_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s12e3comment')
    s12_e4_status = models.BooleanField()
    s12_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s12e4comment')

    s13_e1_va = models.FloatField()
    s13_e1_watt = models.FloatField()
    s13_e1_v = models.FloatField()
    s13_e1_a = models.FloatField()

    s14_e1_type = models.BooleanField()
    s14_e1_er = models.FloatField()
    s14_e1_pe = models.FloatField()
    s14_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ecg, on_delete=models.PROTECT,
                                       related_name='re1s14e1comment')

    s15_e1_aplc = models.IntegerField()
    s15_e1_noaplc = models.IntegerField()
    s15_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='re1s15e1comment')
    s15_e2_aplc = models.IntegerField()
    s15_e2_noaplc = models.IntegerField()
    s15_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                      related_name='re1s15e2comment')

    s16_e1_aplc = models.IntegerField()
    s16_e1_noaplc = models.IntegerField()
    s16_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='re1s16e1comment')
    s16_e2_aplc = models.IntegerField()
    s16_e2_noaplc = models.IntegerField()
    s16_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_safety, on_delete=models.PROTECT,
                                       related_name='re1s16e2comment')

    s17_e1_plc = models.IntegerField()
    s17_e1_pe = models.IntegerField()
    s17_e2_plc = models.IntegerField()
    s17_e2_pe = models.IntegerField()
    s17_e3_plc = models.IntegerField()
    s17_e3_pe = models.IntegerField()
    s17_e4_plc = models.IntegerField()
    s17_e4_pe = models.IntegerField()
    s17_e5_plc = models.IntegerField()
    s17_e5_pe = models.IntegerField()
    s17_e6_plc = models.IntegerField()
    s17_e6_pe = models.IntegerField()
    s17_e7_plc = models.IntegerField()
    s17_e7_pe = models.IntegerField()
    s17_e8_plc = models.IntegerField()
    s17_e8_pe = models.IntegerField()
    s17_e9_plc = models.IntegerField()
    s17_e9_pe = models.IntegerField()
    s17_e10_plc = models.IntegerField()
    s17_e10_pe = models.IntegerField()
    s17_e11_plc = models.IntegerField()
    s17_e11_pe = models.IntegerField()
    s17_e12_plc = models.IntegerField()
    s17_e12_pe = models.IntegerField()

    s18_e1_pac = models.IntegerField()
    s18_e1_pe = models.IntegerField()
    s18_e2_pac = models.IntegerField()
    s18_e2_pe = models.IntegerField()
    s18_e3_pac = models.IntegerField()
    s18_e3_pe = models.IntegerField()
    s18_e4_pac = models.IntegerField()
    s18_e4_pe = models.IntegerField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class flowmeter_1(models.Model):
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE, related_name='fm1licence')
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_flowmeter)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='fm1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()



    s1_e1_rlpm = models.FloatField()
    s1_e2_rlpm = models.FloatField()
    s1_e3_rlpm = models.FloatField()
    s1_e4_rlpm = models.FloatField()
    s1_e5_rlpm = models.FloatField()
    s1_e6_rlpm = models.FloatField()



    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_flowmeter_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rfm1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rfm1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_flowmeter)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)


    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rfm1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()

    s1_e1_rlpm = models.FloatField()
    s1_e2_rlpm = models.FloatField()

    s1_e3_rlpm = models.FloatField()

    s1_e4_rlpm = models.FloatField()

    s1_e5_rlpm = models.FloatField()

    s1_e6_rlpm = models.FloatField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class infusion_pump_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='ip1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_infusion_pump)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='ip1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ip1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ip1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ip1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT,related_name='ip1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='ip1s0e23comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s2e5comment')



    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s3e5comment')


    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT,
                                      related_name='ip1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='ip1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump,on_delete=models.PROTECT, related_name='ip1s5e1comment')

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()
    s7_e1_af = models.IntegerField()
    s7_e2_mmf = models.IntegerField()
    s7_e2_af = models.IntegerField()


    s8_e1_status = models.BooleanField(default=False)


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_infusion_pump_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rip1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rip1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_infusion_pump)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rip1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rip1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rip1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rip1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                       related_name='rip1s0e23comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s2e5comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s3e5comment')

    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_infusion_pump, on_delete=models.PROTECT,
                                      related_name='rip1s5e1comment')

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()
    s7_e1_af = models.IntegerField()
    s7_e2_mmf = models.IntegerField()
    s7_e2_af = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class monometer_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='mm1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monometer)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='mm1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='mm1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='mm1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monometer,on_delete=models.PROTECT,related_name='mm1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='mm1s0e15comment')

    s1_e1_r = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monometer,on_delete=models.PROTECT, related_name='mm1s1e1comment')


    s2_e1_sp = models.IntegerField()
    s2_e1_np = models.ForeignKey(acc.models.quantitive_comment_monometer,on_delete=models.PROTECT, related_name='mm1s2e1comment')
    s2_e2_sp = models.IntegerField()
    s2_e2_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='mm1s2e2comment')
    s2_e3_sp = models.IntegerField()
    s2_e3_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='mm1s2e3comment')
    s2_e4_sp = models.IntegerField()
    s2_e4_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='mm1s2e4comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_monometer_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rmm1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rmm1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monometer)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rmm1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rmm1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rmm1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                       related_name='rmm1s0e15comment')

    s1_e1_r = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                      related_name='rmm1s1e1comment')

    s2_e1_sp = models.IntegerField()
    s2_e1_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='rmm1s2e1comment')
    s2_e2_sp = models.IntegerField()
    s2_e2_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='rmm1s2e2comment')
    s2_e3_sp = models.IntegerField()
    s2_e3_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='rmm1s2e3comment')
    s2_e4_sp = models.IntegerField()
    s2_e4_np = models.ForeignKey(acc.models.quantitive_comment_monometer, on_delete=models.PROTECT,
                                 related_name='rmm1s2e4comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class spo2_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='sp1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_spo2,related_name='sp1totalcomment')
    is_done = models.BooleanField(default=False)


    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='sp1caldev1', default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='sp1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='sp1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='sp1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s1_e1_status = models.BooleanField(default=False)
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s1e1comment')
    s1_e2_status = models.BooleanField(default=False)
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp11s1e2comment')

    s1_e1_spo2 = models.IntegerField()
    s1_e1_pr = models.IntegerField()
    s1_e2_spo2 = models.IntegerField()
    s1_e2_pr = models.IntegerField()
    s1_e3_spo2 = models.IntegerField()
    s1_e3_pr = models.IntegerField()
    s1_e4_spo2 = models.IntegerField()
    s1_e4_pr = models.IntegerField()
    s1_e5_spo2 = models.IntegerField()
    s1_e5_pr = models.IntegerField()
    s1_e6_spo2 = models.IntegerField()
    s1_e6_pr = models.IntegerField()
    s1_e7_spo2 = models.IntegerField()
    s1_e7_pr = models.IntegerField()
    s1_e8_spo2 = models.IntegerField()
    s1_e8_pr = models.IntegerField()
    s1_e9_spo2 = models.IntegerField()
    s1_e9_pr = models.IntegerField()
    s1_e10_spo2 = models.IntegerField()
    s1_e10_pr = models.IntegerField()
    s1_e11_spo2 = models.IntegerField()
    s1_e11_pr = models.IntegerField()
    s1_e12_spo2 = models.IntegerField()
    s1_e12_pr = models.IntegerField()
    s1_e13_spo2 = models.IntegerField()
    s1_e13_pr = models.IntegerField()
    s1_e14_spo2 = models.IntegerField()
    s1_e14_pr = models.IntegerField()

    s2_e1_spo2 = models.IntegerField()
    s2_e1_pr = models.IntegerField()
    s2_e2_spo2 = models.IntegerField()
    s2_e2_pr = models.IntegerField()
    s2_e3_spo2 = models.IntegerField()
    s2_e3_pr = models.IntegerField()
    s2_e4_spo2 = models.IntegerField()
    s2_e4_pr = models.IntegerField()

    s3_e1_accessory = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='sp1s3e1accessory')
    s3_e1_status = models.BooleanField(default=False)
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s3e1comment')

    s4_e1_status = models.BooleanField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s4e1comment')
    s4_e2_status = models.BooleanField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s4e2comment')
    s4_e3_status = models.BooleanField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s4e3comment')
    s4_e4_status = models.BooleanField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s4e4comment')

    s5_e1_va = models.FloatField()
    s5_e1_watt = models.FloatField()
    s5_e1_v = models.FloatField()
    s5_e1_a = models.FloatField()

    s6_e1_type = models.BooleanField()
    s6_e1_er = models.FloatField()
    s6_e1_pe = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s6e1comment')

    s7_e1_aplc = models.IntegerField()
    s7_e1_noaplc = models.IntegerField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s7e1comment')
    s7_e2_aplc = models.IntegerField()
    s7_e2_noaplc = models.IntegerField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='sp1s7e2comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_spo2_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rsp1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rsp1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_spo2)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsp1caldev1', default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsp1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsp1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsp1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s1_e1_status = models.BooleanField(default=False)
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s1e1comment')
    s1_e2_status = models.BooleanField(default=False)
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp11s1e2comment')

    s1_e1_spo2 = models.IntegerField()
    s1_e1_pr = models.IntegerField()
    s1_e2_spo2 = models.IntegerField()
    s1_e2_pr = models.IntegerField()
    s1_e3_spo2 = models.IntegerField()
    s1_e3_pr = models.IntegerField()
    s1_e4_spo2 = models.IntegerField()
    s1_e4_pr = models.IntegerField()
    s1_e5_spo2 = models.IntegerField()
    s1_e5_pr = models.IntegerField()
    s1_e6_spo2 = models.IntegerField()
    s1_e6_pr = models.IntegerField()
    s1_e7_spo2 = models.IntegerField()
    s1_e7_pr = models.IntegerField()
    s1_e8_spo2 = models.IntegerField()
    s1_e8_pr = models.IntegerField()
    s1_e9_spo2 = models.IntegerField()
    s1_e9_pr = models.IntegerField()
    s1_e10_spo2 = models.IntegerField()
    s1_e10_pr = models.IntegerField()
    s1_e11_spo2 = models.IntegerField()
    s1_e11_pr = models.IntegerField()
    s1_e12_spo2 = models.IntegerField()
    s1_e12_pr = models.IntegerField()
    s1_e13_spo2 = models.IntegerField()
    s1_e13_pr = models.IntegerField()
    s1_e14_spo2 = models.IntegerField()
    s1_e14_pr = models.IntegerField()

    s2_e1_spo2 = models.IntegerField()
    s2_e1_pr = models.IntegerField()
    s2_e2_spo2 = models.IntegerField()
    s2_e2_pr = models.IntegerField()
    s2_e3_spo2 = models.IntegerField()
    s2_e3_pr = models.IntegerField()
    s2_e4_spo2 = models.IntegerField()
    s2_e4_pr = models.IntegerField()

    s3_e1_accessory = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='rsp1s3e1accessory')
    s3_e1_status = models.BooleanField(default=False)
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s3e1comment')

    s4_e1_status = models.BooleanField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s4e1comment')
    s4_e2_status = models.BooleanField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s4e2comment')
    s4_e3_status = models.BooleanField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s4e3comment')
    s4_e4_status = models.BooleanField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s4e4comment')

    s5_e1_va = models.FloatField()
    s5_e1_watt = models.FloatField()
    s5_e1_v = models.FloatField()
    s5_e1_a = models.FloatField()

    s6_e1_type = models.BooleanField()
    s6_e1_er = models.FloatField()
    s6_e1_pe = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s6e1comment')

    s7_e1_aplc = models.IntegerField()
    s7_e1_noaplc = models.IntegerField()
    s7_e1_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s7e1comment')
    s7_e2_aplc = models.IntegerField()
    s7_e2_noaplc = models.IntegerField()
    s7_e2_comment = models.ForeignKey(acc.models.quantitive_comment_spo2, on_delete=models.PROTECT,
                                      related_name='rsp1s7e2comment')


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class suction_1(models.Model):
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE, related_name='su1licence')
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_suction, related_name='su1totalcomment')
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='su1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='su1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='su1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='su1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='su1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='su1s0e23comment')

    s1_e1_rr = models.IntegerField()
    s1_e2_rr = models.IntegerField()
    s1_e3_rr = models.IntegerField()
    s1_e4_rr = models.IntegerField()
    s1_e5_rr = models.IntegerField()
    s1_e6_rr = models.IntegerField()
    s1_e7_rr = models.IntegerField()
    s1_e8_rr = models.IntegerField()
    s1_e9_rr = models.IntegerField()
    s1_e10_rr = models.IntegerField()


    s2_e1_rr = models.IntegerField()
    s2_e2_rr = models.IntegerField()
    s2_e3_rr = models.IntegerField()
    s2_e4_rr = models.IntegerField()
    s2_e5_rr = models.IntegerField()
    s2_e6_rr = models.IntegerField()
    s2_e7_rr = models.IntegerField()
    s2_e8_rr = models.IntegerField()


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_suction_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rsu1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rsu1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_suction)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsu1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsu1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsu1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rsu1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                      related_name='rsu1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_suction, on_delete=models.PROTECT,
                                       related_name='rsu1s0e23comment')

    s1_e1_rr = models.IntegerField()
    s1_e2_rr = models.IntegerField()
    s1_e3_rr = models.IntegerField()
    s1_e4_rr = models.IntegerField()
    s1_e5_rr = models.IntegerField()
    s1_e6_rr = models.IntegerField()
    s1_e7_rr = models.IntegerField()
    s1_e8_rr = models.IntegerField()
    s1_e9_rr = models.IntegerField()
    s1_e10_rr = models.IntegerField()

    s2_e1_rr = models.IntegerField()
    s2_e2_rr = models.IntegerField()
    s2_e3_rr = models.IntegerField()
    s2_e4_rr = models.IntegerField()
    s2_e5_rr = models.IntegerField()
    s2_e6_rr = models.IntegerField()
    s2_e7_rr = models.IntegerField()
    s2_e8_rr = models.IntegerField()
    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)


class syringe_pump_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='spo1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_syringe_pump)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='spo1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='spo1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='spo1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='spo1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT,related_name='spo1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='spo1s0e23comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s2e5comment')



    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s3e5comment')


    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT,
                                      related_name='spo1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='spo1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump,on_delete=models.PROTECT, related_name='spo1s5e1comment')

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()
    s7_e1_af = models.IntegerField()
    s7_e2_mmf = models.IntegerField()
    s7_e2_af = models.IntegerField()


    s8_e1_status = models.BooleanField(default=False)


    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_syringe_pump_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rspo1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rspo1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_syringe_pump)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rspo1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rspo1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rspo1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rspo1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e21comment')
    s0_e22_status = models.BooleanField(default=False)
    s0_e22_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e22comment')
    s0_e23_status = models.BooleanField(default=False)
    s0_e23_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                       related_name='rspo1s0e23comment')

    s1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s2e2comment')
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s2e3comment')
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s2e4comment')
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s2e5comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s3e2comment')
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s3e3comment')
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s3e4comment')
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s3e5comment')

    s4_e1_dclc = models.IntegerField()
    s4_e1_aclc = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e1comment')

    s4_e2_dclc = models.IntegerField()
    s4_e2_aclc = models.IntegerField()
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e2comment')
    s4_e3_dclc = models.IntegerField()
    s4_e3_aclc = models.IntegerField()
    s4_e3_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e3comment')
    s4_e4_dclc = models.IntegerField()
    s4_e4_aclc = models.IntegerField()
    s4_e4_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e4comment')
    s4_e5_dclc = models.IntegerField()
    s4_e5_aclc = models.IntegerField()
    s4_e5_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e5comment')
    s4_e6_dclc = models.IntegerField()
    s4_e6_aclc = models.IntegerField()
    s4_e6_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s4e6comment')

    s5_e1_cflc = models.IntegerField()
    s5_e1_bflc = models.IntegerField()
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_syringe_pump, on_delete=models.PROTECT,
                                      related_name='rspo1s5e1comment')

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()
    s7_e1_af = models.IntegerField()
    s7_e2_mmf = models.IntegerField()
    s7_e2_af = models.IntegerField()

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class electrocauter_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='ec1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_electrocouter)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='ec1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ec1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ec1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ec1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()
    cal_dev5 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ec1caldev5')
    cal_dev_5_cd = models.DateField()
    cal_dev_5_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter,on_delete=models.PROTECT,related_name='ec1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s0e17comment')


    s1_res = models.IntegerField()

    s2_e1 = models.IntegerField()
    s2_e2 = models.IntegerField()

    s3a_e1_1 = models.IntegerField()
    s3a_e1_s = models.IntegerField()
    s3a_e1_m = models.IntegerField()
    s3a_e2_1 = models.IntegerField()
    s3a_e2_s = models.IntegerField()
    s3a_e2_m = models.IntegerField()
    s3a_e3_1 = models.IntegerField()
    s3a_e3_s = models.IntegerField()
    s3a_e3_m = models.IntegerField()
    s3a_e4_1 = models.IntegerField(default=-1)
    s3a_e4_s = models.IntegerField(default=-1)
    s3a_e4_m = models.IntegerField(default=-1)
    s3a_e5_1 = models.IntegerField(default=-1)
    s3a_e5_s = models.IntegerField(default=-1)
    s3a_e5_m = models.IntegerField(default=-1)
    s3a_e6_1 = models.IntegerField(default=-1)
    s3a_e6_s = models.IntegerField(default=-1)
    s3a_e6_m = models.IntegerField(default=-1)
    s3a_e7_1 = models.IntegerField(default=-1)
    s3a_e7_s = models.IntegerField(default=-1)
    s3a_e7_m = models.IntegerField(default=-1)

    s3b_e1_1 = models.IntegerField()
    s3b_e1_s = models.IntegerField()
    s3b_e1_m = models.IntegerField()
    s3b_e2_1 = models.IntegerField()
    s3b_e2_s = models.IntegerField()
    s3b_e2_m = models.IntegerField()
    s3b_e3_1 = models.IntegerField()
    s3b_e3_s = models.IntegerField()
    s3b_e3_m = models.IntegerField()
    s3b_e4_1 = models.IntegerField(default=-1)
    s3b_e4_s = models.IntegerField(default=-1)
    s3b_e4_m = models.IntegerField(default=-1)
    s3b_e5_1 = models.IntegerField(default=-1)
    s3b_e5_s = models.IntegerField(default=-1)
    s3b_e5_m = models.IntegerField(default=-1)
    s3b_e6_1 = models.IntegerField(default=-1)
    s3b_e6_s = models.IntegerField(default=-1)
    s3b_e6_m = models.IntegerField(default=-1)
    s3b_e7_1 = models.IntegerField(default=-1)
    s3b_e7_s = models.IntegerField(default=-1)
    s3b_e7_m = models.IntegerField(default=-1)

    s3c_e1_1 = models.IntegerField()
    s3c_e1_s = models.IntegerField()
    s3c_e1_m = models.IntegerField()
    s3c_e2_1 = models.IntegerField()
    s3c_e2_s = models.IntegerField()
    s3c_e2_m = models.IntegerField()
    s3c_e3_1 = models.IntegerField()
    s3c_e3_s = models.IntegerField()
    s3c_e3_m = models.IntegerField()
    s3c_e4_1 = models.IntegerField(default=-1)
    s3c_e4_s = models.IntegerField(default=-1)
    s3c_e4_m = models.IntegerField(default=-1)
    s3c_e5_1 = models.IntegerField(default=-1)
    s3c_e5_s = models.IntegerField(default=-1)
    s3c_e5_m = models.IntegerField(default=-1)
    s3c_e6_1 = models.IntegerField(default=-1)
    s3c_e6_s = models.IntegerField(default=-1)
    s3c_e6_m = models.IntegerField(default=-1)
    s3c_e7_1 = models.IntegerField(default=-1)
    s3c_e7_s = models.IntegerField(default=-1)
    s3c_e7_m = models.IntegerField(default=-1)

    s3d_e1_1 = models.IntegerField()
    s3d_e1_s = models.IntegerField()
    s3d_e1_m = models.IntegerField()
    s3d_e2_1 = models.IntegerField()
    s3d_e2_s = models.IntegerField()
    s3d_e2_m = models.IntegerField()
    s3d_e3_1 = models.IntegerField()
    s3d_e3_s = models.IntegerField()
    s3d_e3_m = models.IntegerField()
    s3d_e4_1 = models.IntegerField(default=-1)
    s3d_e4_s = models.IntegerField(default=-1)
    s3d_e4_m = models.IntegerField(default=-1)
    s3d_e5_1 = models.IntegerField(default=-1)
    s3d_e5_s = models.IntegerField(default=-1)
    s3d_e5_m = models.IntegerField(default=-1)
    s3d_e6_1 = models.IntegerField(default=-1)
    s3d_e6_s = models.IntegerField(default=-1)
    s3d_e6_m = models.IntegerField(default=-1)
    s3d_e7_1 = models.IntegerField(default=-1)
    s3d_e7_s = models.IntegerField(default=-1)
    s3d_e7_m = models.IntegerField(default=-1)

    s3e_e1_1 = models.IntegerField()
    s3e_e1_s = models.IntegerField()
    s3e_e1_m = models.IntegerField()
    s3e_e2_1 = models.IntegerField()
    s3e_e2_s = models.IntegerField()
    s3e_e2_m = models.IntegerField()
    s3e_e3_1 = models.IntegerField()
    s3e_e3_s = models.IntegerField()
    s3e_e3_m = models.IntegerField()
    s3e_e4_1 = models.IntegerField(default=-1)
    s3e_e4_s = models.IntegerField(default=-1)
    s3e_e4_m = models.IntegerField(default=-1)
    s3e_e5_1 = models.IntegerField(default=-1)
    s3e_e5_s = models.IntegerField(default=-1)
    s3e_e5_m = models.IntegerField(default=-1)
    s3e_e6_1 = models.IntegerField(default=-1)
    s3e_e6_s = models.IntegerField(default=-1)
    s3e_e6_m = models.IntegerField(default=-1)
    s3e_e7_1 = models.IntegerField(default=-1)
    s3e_e7_s = models.IntegerField(default=-1)
    s3e_e7_m = models.IntegerField(default=-1)

    s3f_e1_1 = models.IntegerField(default=-1)
    s3f_e1_s = models.IntegerField(default=-1)
    s3f_e1_m = models.IntegerField(default=-1)
    s3f_e2_1 = models.IntegerField(default=-1)
    s3f_e2_s = models.IntegerField(default=-1)
    s3f_e2_m = models.IntegerField(default=-1)
    s3f_e3_1 = models.IntegerField(default=-1)
    s3f_e3_s = models.IntegerField(default=-1)
    s3f_e3_m = models.IntegerField(default=-1)
    s3f_e4_1 = models.IntegerField(default=-1)
    s3f_e4_s = models.IntegerField(default=-1)
    s3f_e4_m = models.IntegerField(default=-1)
    s3f_e5_1 = models.IntegerField(default=-1)
    s3f_e5_s = models.IntegerField(default=-1)
    s3f_e5_m = models.IntegerField(default=-1)
    s3f_e6_1 = models.IntegerField(default=-1)
    s3f_e6_s = models.IntegerField(default=-1)
    s3f_e6_m = models.IntegerField(default=-1)
    s3f_e7_1 = models.IntegerField(default=-1)
    s3f_e7_s = models.IntegerField(default=-1)
    s3f_e7_m = models.IntegerField(default=-1)


    s4a_e1 = models.IntegerField(default=-1)
    s4a_e2 = models.IntegerField(default=-1)
    s4a_e3 = models.IntegerField(default=-1)

    s4b_e1 = models.IntegerField(default=-1)
    s4b_e2 = models.IntegerField(default=-1)
    s4b_e3 = models.IntegerField(default=-1)

    s4c_e1 = models.IntegerField()
    s4c_e2 = models.IntegerField()
    s4c_e3 = models.IntegerField()

    s4d_e1 = models.IntegerField()
    s4d_e2 = models.IntegerField()
    s4d_e3 = models.IntegerField()

    s4e_e1 = models.IntegerField()
    s4e_e2 = models.IntegerField()
    s4e_e3 = models.IntegerField()

    s4f_e1 = models.IntegerField()
    s4f_e2 = models.IntegerField()
    s4f_e3 = models.IntegerField()

    s4g_e1 = models.IntegerField()
    s4g_e2 = models.IntegerField()
    s4g_e3 = models.IntegerField(default=-1)

    s4h_e1 = models.IntegerField(default=-1)
    s4h_e2 = models.IntegerField(default=-1)
    s4h_e3 = models.IntegerField(default=-1)

    s4i_e1 = models.IntegerField(default=-1)
    s4i_e2 = models.IntegerField(default=-1)
    s4i_e3 = models.IntegerField(default=-1)

    s4j_e1 = models.IntegerField(default=-1)
    s4j_e2 = models.IntegerField(default=-1)
    s4j_e3 = models.IntegerField(default=-1)

    s4k_e1 = models.IntegerField(default=-1)
    s4k_e2 = models.IntegerField(default=-1)
    s4k_e3 = models.IntegerField(default=-1)

    s4l_e1 = models.IntegerField(default=-1)
    s4l_e2 = models.IntegerField(default=-1)
    s4l_e3 = models.IntegerField(default=-1)

    s4m_e1 = models.IntegerField()
    s4m_e2 = models.IntegerField()
    s4m_e3 = models.IntegerField(default=-1)

    s4n_e1 = models.IntegerField()
    s4n_e2 = models.IntegerField()
    s4n_e3 = models.IntegerField(default=-1)

    s4o_e1 = models.IntegerField(default=-1)
    s4o_e2 = models.IntegerField(default=-1)
    s4o_e3 = models.IntegerField(default=-1)

    s4p_e1 = models.IntegerField(default=-1)
    s4p_e2 = models.IntegerField(default=-1)
    s4p_e3 = models.IntegerField(default=-1)

    s4q_e1 = models.IntegerField(default=-1)
    s4q_e2 = models.IntegerField(default=-1)
    s4q_e3 = models.IntegerField(default=-1)

    s4r_e1 = models.IntegerField(default=-1)
    s4r_e2 = models.IntegerField(default=-1)
    s4r_e3 = models.IntegerField(default=-1)



    s5a_e1 = models.IntegerField()
    s5a_e2 = models.IntegerField()
    s5a_e3 = models.IntegerField(default=-1)

    s5b_e1 = models.IntegerField()
    s5b_e2 = models.IntegerField()
    s5b_e3 = models.IntegerField(default=-1)

    s5c_e1 = models.IntegerField(default=-1)
    s5c_e2 = models.IntegerField(default=-1)
    s5c_e3 = models.IntegerField(default=-1)

    test_type = models.ForeignKey(acc.models.test_type, on_delete=models.CASCADE, related_name='ec1tt')

    s11_e1_res = models.IntegerField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s11e1comment')
    s11_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s11e2comment')


    s12_e1_lc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='ec1s12e1comment')
    s12_e2_lc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s12e2comment')

    s13_e1_lc = models.IntegerField()
    s13_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s13e1comment')
    s13_e2_lc = models.IntegerField()
    s13_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s13e2comment')
    s14_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='ec1s14_t')

    s14_e1_lc1 = models.IntegerField()
    s14_e1_lc2 = models.IntegerField()
    s14_e1_lc3 = models.IntegerField()
    s14_e1_lc4 = models.IntegerField()
    s14_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s14e1comment')
    s14_e2_lc1 = models.IntegerField()
    s14_e2_lc2 = models.IntegerField()
    s14_e2_lc3 = models.IntegerField()
    s14_e2_lc4 = models.IntegerField()
    s14_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s14e2comment')

    s15_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='ec1s15_t')

    s15_e1_lc1 = models.IntegerField()
    s15_e1_lc2 = models.IntegerField()
    s15_e1_lc3 = models.IntegerField()
    s15_e1_lc4 = models.IntegerField()
    s15_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s15e1comment')
    s15_e2_lc1 = models.IntegerField()
    s15_e2_lc2 = models.IntegerField()
    s15_e2_lc3 = models.IntegerField()
    s15_e2_lc4 = models.IntegerField()
    s15_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s15e2comment')

    s16_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='ec1s16_t')

    s16_e1_lc1 = models.IntegerField()
    s16_e1_lc2 = models.IntegerField()
    s16_e1_lc3 = models.IntegerField()
    s16_e1_lc4 = models.IntegerField()
    s16_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='ec1s16e1comment')

    se_e1_title = models.CharField(max_length=20,default='-')
    se_e1_comment = models.CharField(max_length=40,default='-')
    se_e2_title = models.CharField(max_length=20,default='-')
    se_e2_comment = models.CharField(max_length=40,default='-')
    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_electrocauter_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rec1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rec1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_electrocouter)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rec1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rec1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rec1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rec1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()
    cal_dev5 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='rec1caldev5')
    cal_dev_5_cd = models.DateField()
    cal_dev_5_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                      related_name='rec1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s0e17comment')

    s1_res = models.IntegerField()

    s2_e1 = models.IntegerField()
    s2_e2 = models.IntegerField()

    s3a_e1_1 = models.IntegerField()
    s3a_e1_s = models.IntegerField()
    s3a_e1_m = models.IntegerField()
    s3a_e2_1 = models.IntegerField()
    s3a_e2_s = models.IntegerField()
    s3a_e2_m = models.IntegerField()
    s3a_e3_1 = models.IntegerField()
    s3a_e3_s = models.IntegerField()
    s3a_e3_m = models.IntegerField()
    s3a_e4_1 = models.IntegerField(default=-1)
    s3a_e4_s = models.IntegerField(default=-1)
    s3a_e4_m = models.IntegerField(default=-1)
    s3a_e5_1 = models.IntegerField(default=-1)
    s3a_e5_s = models.IntegerField(default=-1)
    s3a_e5_m = models.IntegerField(default=-1)
    s3a_e6_1 = models.IntegerField(default=-1)
    s3a_e6_s = models.IntegerField(default=-1)
    s3a_e6_m = models.IntegerField(default=-1)
    s3a_e7_1 = models.IntegerField(default=-1)
    s3a_e7_s = models.IntegerField(default=-1)
    s3a_e7_m = models.IntegerField(default=-1)

    s3b_e1_1 = models.IntegerField()
    s3b_e1_s = models.IntegerField()
    s3b_e1_m = models.IntegerField()
    s3b_e2_1 = models.IntegerField()
    s3b_e2_s = models.IntegerField()
    s3b_e2_m = models.IntegerField()
    s3b_e3_1 = models.IntegerField()
    s3b_e3_s = models.IntegerField()
    s3b_e3_m = models.IntegerField()
    s3b_e4_1 = models.IntegerField(default=-1)
    s3b_e4_s = models.IntegerField(default=-1)
    s3b_e4_m = models.IntegerField(default=-1)
    s3b_e5_1 = models.IntegerField(default=-1)
    s3b_e5_s = models.IntegerField(default=-1)
    s3b_e5_m = models.IntegerField(default=-1)
    s3b_e6_1 = models.IntegerField(default=-1)
    s3b_e6_s = models.IntegerField(default=-1)
    s3b_e6_m = models.IntegerField(default=-1)
    s3b_e7_1 = models.IntegerField(default=-1)
    s3b_e7_s = models.IntegerField(default=-1)
    s3b_e7_m = models.IntegerField(default=-1)

    s3c_e1_1 = models.IntegerField()
    s3c_e1_s = models.IntegerField()
    s3c_e1_m = models.IntegerField()
    s3c_e2_1 = models.IntegerField()
    s3c_e2_s = models.IntegerField()
    s3c_e2_m = models.IntegerField()
    s3c_e3_1 = models.IntegerField()
    s3c_e3_s = models.IntegerField()
    s3c_e3_m = models.IntegerField()
    s3c_e4_1 = models.IntegerField(default=-1)
    s3c_e4_s = models.IntegerField(default=-1)
    s3c_e4_m = models.IntegerField(default=-1)
    s3c_e5_1 = models.IntegerField(default=-1)
    s3c_e5_s = models.IntegerField(default=-1)
    s3c_e5_m = models.IntegerField(default=-1)
    s3c_e6_1 = models.IntegerField(default=-1)
    s3c_e6_s = models.IntegerField(default=-1)
    s3c_e6_m = models.IntegerField(default=-1)
    s3c_e7_1 = models.IntegerField(default=-1)
    s3c_e7_s = models.IntegerField(default=-1)
    s3c_e7_m = models.IntegerField(default=-1)

    s3d_e1_1 = models.IntegerField()
    s3d_e1_s = models.IntegerField()
    s3d_e1_m = models.IntegerField()
    s3d_e2_1 = models.IntegerField()
    s3d_e2_s = models.IntegerField()
    s3d_e2_m = models.IntegerField()
    s3d_e3_1 = models.IntegerField()
    s3d_e3_s = models.IntegerField()
    s3d_e3_m = models.IntegerField()
    s3d_e4_1 = models.IntegerField(default=-1)
    s3d_e4_s = models.IntegerField(default=-1)
    s3d_e4_m = models.IntegerField(default=-1)
    s3d_e5_1 = models.IntegerField(default=-1)
    s3d_e5_s = models.IntegerField(default=-1)
    s3d_e5_m = models.IntegerField(default=-1)
    s3d_e6_1 = models.IntegerField(default=-1)
    s3d_e6_s = models.IntegerField(default=-1)
    s3d_e6_m = models.IntegerField(default=-1)
    s3d_e7_1 = models.IntegerField(default=-1)
    s3d_e7_s = models.IntegerField(default=-1)
    s3d_e7_m = models.IntegerField(default=-1)

    s3e_e1_1 = models.IntegerField()
    s3e_e1_s = models.IntegerField()
    s3e_e1_m = models.IntegerField()
    s3e_e2_1 = models.IntegerField()
    s3e_e2_s = models.IntegerField()
    s3e_e2_m = models.IntegerField()
    s3e_e3_1 = models.IntegerField()
    s3e_e3_s = models.IntegerField()
    s3e_e3_m = models.IntegerField()
    s3e_e4_1 = models.IntegerField(default=-1)
    s3e_e4_s = models.IntegerField(default=-1)
    s3e_e4_m = models.IntegerField(default=-1)
    s3e_e5_1 = models.IntegerField(default=-1)
    s3e_e5_s = models.IntegerField(default=-1)
    s3e_e5_m = models.IntegerField(default=-1)
    s3e_e6_1 = models.IntegerField(default=-1)
    s3e_e6_s = models.IntegerField(default=-1)
    s3e_e6_m = models.IntegerField(default=-1)
    s3e_e7_1 = models.IntegerField(default=-1)
    s3e_e7_s = models.IntegerField(default=-1)
    s3e_e7_m = models.IntegerField(default=-1)

    s3f_e1_1 = models.IntegerField(default=-1)
    s3f_e1_s = models.IntegerField(default=-1)
    s3f_e1_m = models.IntegerField(default=-1)
    s3f_e2_1 = models.IntegerField(default=-1)
    s3f_e2_s = models.IntegerField(default=-1)
    s3f_e2_m = models.IntegerField(default=-1)
    s3f_e3_1 = models.IntegerField(default=-1)
    s3f_e3_s = models.IntegerField(default=-1)
    s3f_e3_m = models.IntegerField(default=-1)
    s3f_e4_1 = models.IntegerField(default=-1)
    s3f_e4_s = models.IntegerField(default=-1)
    s3f_e4_m = models.IntegerField(default=-1)
    s3f_e5_1 = models.IntegerField(default=-1)
    s3f_e5_s = models.IntegerField(default=-1)
    s3f_e5_m = models.IntegerField(default=-1)
    s3f_e6_1 = models.IntegerField(default=-1)
    s3f_e6_s = models.IntegerField(default=-1)
    s3f_e6_m = models.IntegerField(default=-1)
    s3f_e7_1 = models.IntegerField(default=-1)
    s3f_e7_s = models.IntegerField(default=-1)
    s3f_e7_m = models.IntegerField(default=-1)

    s4a_e1 = models.IntegerField(default=-1)
    s4a_e2 = models.IntegerField(default=-1)
    s4a_e3 = models.IntegerField(default=-1)

    s4b_e1 = models.IntegerField(default=-1)
    s4b_e2 = models.IntegerField(default=-1)
    s4b_e3 = models.IntegerField(default=-1)

    s4c_e1 = models.IntegerField()
    s4c_e2 = models.IntegerField()
    s4c_e3 = models.IntegerField()

    s4d_e1 = models.IntegerField()
    s4d_e2 = models.IntegerField()
    s4d_e3 = models.IntegerField()

    s4e_e1 = models.IntegerField()
    s4e_e2 = models.IntegerField()
    s4e_e3 = models.IntegerField()

    s4f_e1 = models.IntegerField()
    s4f_e2 = models.IntegerField()
    s4f_e3 = models.IntegerField()

    s4g_e1 = models.IntegerField()
    s4g_e2 = models.IntegerField()
    s4g_e3 = models.IntegerField(default=-1)

    s4h_e1 = models.IntegerField(default=-1)
    s4h_e2 = models.IntegerField(default=-1)
    s4h_e3 = models.IntegerField(default=-1)

    s4i_e1 = models.IntegerField(default=-1)
    s4i_e2 = models.IntegerField(default=-1)
    s4i_e3 = models.IntegerField(default=-1)

    s4j_e1 = models.IntegerField(default=-1)
    s4j_e2 = models.IntegerField(default=-1)
    s4j_e3 = models.IntegerField(default=-1)

    s4k_e1 = models.IntegerField(default=-1)
    s4k_e2 = models.IntegerField(default=-1)
    s4k_e3 = models.IntegerField(default=-1)

    s4l_e1 = models.IntegerField(default=-1)
    s4l_e2 = models.IntegerField(default=-1)
    s4l_e3 = models.IntegerField(default=-1)

    s4m_e1 = models.IntegerField()
    s4m_e2 = models.IntegerField()
    s4m_e3 = models.IntegerField(default=-1)

    s4n_e1 = models.IntegerField()
    s4n_e2 = models.IntegerField()
    s4n_e3 = models.IntegerField(default=-1)

    s4o_e1 = models.IntegerField(default=-1)
    s4o_e2 = models.IntegerField(default=-1)
    s4o_e3 = models.IntegerField(default=-1)

    s4p_e1 = models.IntegerField(default=-1)
    s4p_e2 = models.IntegerField(default=-1)
    s4p_e3 = models.IntegerField(default=-1)

    s4q_e1 = models.IntegerField(default=-1)
    s4q_e2 = models.IntegerField(default=-1)
    s4q_e3 = models.IntegerField(default=-1)

    s4r_e1 = models.IntegerField(default=-1)
    s4r_e2 = models.IntegerField(default=-1)
    s4r_e3 = models.IntegerField(default=-1)

    s5a_e1 = models.IntegerField()
    s5a_e2 = models.IntegerField()
    s5a_e3 = models.IntegerField(default=-1)

    s5b_e1 = models.IntegerField()
    s5b_e2 = models.IntegerField()
    s5b_e3 = models.IntegerField(default=-1)

    s5c_e1 = models.IntegerField(default=-1)
    s5c_e2 = models.IntegerField(default=-1)
    s5c_e3 = models.IntegerField(default=-1)

    test_type = models.ForeignKey(acc.models.test_type, on_delete=models.CASCADE, related_name='rec1tt')

    s11_e1_res = models.IntegerField()
    s11_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s11e1comment')
    s11_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s11e2comment')

    s12_e1_lc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s12e1comment')
    s12_e2_lc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s12e2comment')

    s13_e1_lc = models.IntegerField()
    s13_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s13e1comment')
    s13_e2_lc = models.IntegerField()
    s13_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s13e2comment')
    s14_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE, related_name='rec1s14_t')

    s14_e1_lc1 = models.IntegerField()
    s14_e1_lc2 = models.IntegerField()
    s14_e1_lc3 = models.IntegerField()
    s14_e1_lc4 = models.IntegerField()
    s14_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s14e1comment')
    s14_e2_lc1 = models.IntegerField()
    s14_e2_lc2 = models.IntegerField()
    s14_e2_lc3 = models.IntegerField()
    s14_e2_lc4 = models.IntegerField()
    s14_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s14e2comment')

    s15_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE, related_name='rec1s15_t')

    s15_e1_lc1 = models.IntegerField()
    s15_e1_lc2 = models.IntegerField()
    s15_e1_lc3 = models.IntegerField()
    s15_e1_lc4 = models.IntegerField()
    s15_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s15e1comment')
    s15_e2_lc1 = models.IntegerField()
    s15_e2_lc2 = models.IntegerField()
    s15_e2_lc3 = models.IntegerField()
    s15_e2_lc4 = models.IntegerField()
    s15_e2_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s15e2comment')

    s16_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE, related_name='rec1s16_t')

    s16_e1_lc1 = models.IntegerField()
    s16_e1_lc2 = models.IntegerField()
    s16_e1_lc3 = models.IntegerField()
    s16_e1_lc4 = models.IntegerField()
    s16_e1_comment = models.ForeignKey(acc.models.quantitive_comment_electrocouter, on_delete=models.PROTECT,
                                       related_name='rec1s16e1comment')

    se_e1_title = models.CharField(max_length=20, default='-')
    se_e1_comment = models.CharField(max_length=40, default='-')
    se_e2_title = models.CharField(max_length=20, default='-')
    se_e2_comment = models.CharField(max_length=40, default='-')
    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)

class ventilator_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE,related_name='ven1licence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_ventilator)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device,on_delete=models.PROTECT,related_name='ven1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()


    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator,on_delete=models.PROTECT,related_name='ven1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e21comment')


    test_type = models.ForeignKey(acc.models.test_type, on_delete=models.CASCADE, related_name='ven1tt')

    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s1e2comment')


    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s2e2comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s3e2comment')
    s4_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='ven1s4_t')

    s4_e1_lcac = models.IntegerField(default=-1)
    s4_e1_lcdc = models.IntegerField(default=-1)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s4e1comment')
    s4_e2_lcac = models.IntegerField(default=-1)
    s4_e2_lcdc = models.IntegerField(default=-1)
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s4e2comment')

    s5_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE,related_name='ven1s5_t')

    s2_e1_lcbf = models.IntegerField(default=-1)
    s5_e1_lccf = models.IntegerField(default=-1)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s5e1comment')
    s5_e2_lc = models.IntegerField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s5e2comment')

    s6_e1_rff = models.IntegerField()
    s6_e1_ffr = models.IntegerField()

    s7_e1_si1 = models.IntegerField()
    s7_e1_si2 = models.IntegerField()
    s7_e1_si3 = models.IntegerField()
    s7_e1_si4 = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    s9_e1 = models.IntegerField(default=-1)

    s10_e1 = models.IntegerField(default=-1)

    s11_e1_status = models.BooleanField(default=False)

    s12_e1 = models.IntegerField(default=-1)
    s12_e2 = models.IntegerField(default=-1)


    s13_e1 = models.IntegerField(default=-1)
    s13_e2 = models.IntegerField(default=-1)

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()
    s14_e3 = models.IntegerField()

    s15_e1 = models.IntegerField()
    s15_e2 = models.IntegerField()

    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()
    s16_e3 = models.IntegerField()
    s16_e4 = models.IntegerField()
    s16_e5 = models.IntegerField()
    s16_e6 = models.IntegerField()

    def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
class recal_ventilator_1(models.Model):

    device = models.ForeignKey(acc.models.All_Device,on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request,on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.PROTECT,related_name='rec1licence')
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE,related_name='rec1reflicence')
    record = models.ForeignKey(acc.models.record,on_delete=models.CASCADE)
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_electrocouter)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev1')
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev2')
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev3')
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ven1caldev4')
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_status = models.BooleanField(default=False)
    s0_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e1comment')
    s0_e2_status = models.BooleanField(default=False)
    s0_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e2comment')
    s0_e3_status = models.BooleanField(default=False)
    s0_e3_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e3comment')
    s0_e4_status = models.BooleanField(default=False)
    s0_e4_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e4comment')
    s0_e5_status = models.BooleanField(default=False)
    s0_e5_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e5comment')
    s0_e6_status = models.BooleanField(default=False)
    s0_e6_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e6comment')
    s0_e7_status = models.BooleanField(default=False)
    s0_e7_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e7comment')
    s0_e8_status = models.BooleanField(default=False)
    s0_e8_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e8comment')
    s0_e9_status = models.BooleanField(default=False)
    s0_e9_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s0e9comment')
    s0_e10_status = models.BooleanField(default=False)
    s0_e10_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e10comment')
    s0_e11_status = models.BooleanField(default=False)
    s0_e11_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e11comment')
    s0_e12_status = models.BooleanField(default=False)
    s0_e12_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e12comment')
    s0_e13_status = models.BooleanField(default=False)
    s0_e13_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e13comment')
    s0_e14_status = models.BooleanField(default=False)
    s0_e14_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e14comment')
    s0_e15_status = models.BooleanField(default=False)
    s0_e15_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e15comment')
    s0_e16_status = models.BooleanField(default=False)
    s0_e16_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e16comment')
    s0_e17_status = models.BooleanField(default=False)
    s0_e17_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e17comment')
    s0_e18_status = models.BooleanField(default=False)
    s0_e18_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e18comment')
    s0_e19_status = models.BooleanField(default=False)
    s0_e19_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e19comment')
    s0_e20_status = models.BooleanField(default=False)
    s0_e20_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e20comment')
    s0_e21_status = models.BooleanField(default=False)
    s0_e21_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                       related_name='ven1s0e21comment')

    test_type = models.ForeignKey(acc.models.test_type, on_delete=models.CASCADE, related_name='ven1tt')

    s1_e1_res = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s1e1comment')
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s2e1comment')
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s2e2comment')

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s3e1comment')
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s3e2comment')
    s4_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE, related_name='ven1s4_t')

    s4_e1_lcac = models.IntegerField(default=-1)
    s4_e1_lcdc = models.IntegerField(default=-1)
    s4_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s4e1comment')
    s4_e2_lcac = models.IntegerField(default=-1)
    s4_e2_lcdc = models.IntegerField(default=-1)
    s4_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s4e2comment')

    s5_type = models.ForeignKey(acc.models.test_type2, on_delete=models.CASCADE, related_name='ven1s5_t')

    s2_e1_lcbf = models.IntegerField(default=-1)
    s5_e1_lccf = models.IntegerField(default=-1)
    s5_e1_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s5e1comment')
    s5_e2_lc = models.IntegerField()
    s5_e2_comment = models.ForeignKey(acc.models.quantitive_comment_ventilator, on_delete=models.PROTECT,
                                      related_name='ven1s5e2comment')

    s6_e1_rff = models.IntegerField()
    s6_e1_ffr = models.IntegerField()

    s7_e1_si1 = models.IntegerField()
    s7_e1_si2 = models.IntegerField()
    s7_e1_si3 = models.IntegerField()
    s7_e1_si4 = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    s9_e1 = models.IntegerField(default=-1)

    s10_e1 = models.IntegerField(default=-1)

    s11_e1_status = models.BooleanField(default=False)

    s12_e1 = models.IntegerField(default=-1)
    s12_e2 = models.IntegerField(default=-1)

    s13_e1 = models.IntegerField(default=-1)
    s13_e2 = models.IntegerField(default=-1)

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()
    s14_e3 = models.IntegerField()

    s15_e1 = models.IntegerField()
    s15_e2 = models.IntegerField()

    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()
    s16_e3 = models.IntegerField()
    s16_e4 = models.IntegerField()
    s16_e5 = models.IntegerField()
    s16_e6 = models.IntegerField()


def __str__(self):
        return 'Licence: ' + str(self.licence) + ' - ' + str(self.device.name)
