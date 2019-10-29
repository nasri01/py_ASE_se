from django.db import models

import acc.models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

class cant_test(models.Model):
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE, related_name='ctr')
    totalcomment = models.ManyToManyField(acc.models.comment_cant_test, related_name='cttotalcomment')
    
class monitor_spo2_1(models.Model):
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE, related_name='ms1rr')

    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    licence = models.ForeignKey(acc.models.licence, on_delete=models.CASCADE, related_name='ms1licence')
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE, related_name='ms1r')
    totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_spo2, related_name='ms1totalcomment')
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ms1caldev1', default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ms1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(acc.models.Cal_device, on_delete=models.PROTECT, related_name='ms1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2, on_delete=models.PROTECT,
                                      related_name='ms1s1e1comment', default=1)
    s1_e2_comment = models.ForeignKey(acc.models.quantitive_comment_monitor_spo2, on_delete=models.PROTECT,
                                      related_name='ms11s1e2comment', default=1)

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

    s4_e1_acc = models.ForeignKey(acc.models.accessory, on_delete=models.PROTECT, related_name='ms1s4e1accessory',default=1)
    s4_e1_comment = models.ForeignKey(acc.mo