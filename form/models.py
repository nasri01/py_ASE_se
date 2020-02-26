from django.db import models

import acc.models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class CantTest(models.Model):
    class Meta:
        verbose_name_plural = "1_Can,t Test"
    tt = models.ForeignKey(acc.models.AdTestType0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ctr')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    is_recal = models.BooleanField(default=False)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT, default=4)

    def __str__(self):
        return 'CantTest : ' + str(self.tt) + str(self.device.name.name)


class MonitorSpo2_1(models.Model):
    class Meta:
        verbose_name_plural = "Monitor SPO2"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ms1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='ms1licence')
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ms1r')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ms1caldev1', default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ms1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ms1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ms1s1e1comment', default=1)
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
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

    s4_e1_acc = models.ForeignKey(
        acc.models.Accessory, on_delete=models.PROTECT, related_name='ms1s4e1accessory', default=1)
    s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ms1s4e1comment', default=2)

    def __str__(self):
        return 'MonitorSpo2 : ' + str(self.Licence)


class MonitorECG_1(models.Model):
    class Meta:
        verbose_name_plural = "Monitor ECG"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='me1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='me1licence')
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='me1r')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='me1caldev1', default=5)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='me1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='me1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_hr = models.IntegerField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e1comment', default=1)
    s1_e2_hr = models.IntegerField()
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e2comment', default=1)
    s1_e3_hr = models.IntegerField()
    s1_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e3comment', default=1)
    s1_e4_hr = models.IntegerField()
    s1_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e4comment', default=1)
    s1_e5_hr = models.IntegerField()
    s1_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e5comment', default=1)
    s1_e6_hr = models.IntegerField()
    s1_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e6comment', default=1)
    s1_e7_hr = models.IntegerField()
    s1_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e7comment', default=1)
    s1_e8_hr = models.IntegerField()
    s1_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s1e8comment', default=1)

    s2_e1_hr = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e1comment', default=1)
    s2_e2_hr = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e2comment', default=1)
    s2_e3_hr = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e3comment', default=1)
    s2_e4_hr = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e4comment', default=1)
    s2_e5_hr = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e5comment', default=1)
    s2_e6_hr = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e6comment', default=1)
    s2_e7_hr = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e7comment', default=1)
    s2_e8_hr = models.IntegerField()
    s2_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e8comment', default=1)
    s2_e9_hr = models.IntegerField()
    s2_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s2e9comment', default=1)
    s2_e10_hr = models.IntegerField()
    s2_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='me1s2e10comment', default=1)

    s3_e1_hr = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e1comment', default=1)
    s3_e2_hr = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e2comment', default=1)
    s3_e3_hr = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e3comment', default=1)
    s3_e4_hr = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e4comment', default=1)
    s3_e5_hr = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e5comment', default=1)
    s3_e6_hr = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e6comment', default=1)
    s3_e7_hr = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e7comment', default=1)
    s3_e8_hr = models.IntegerField()
    s3_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e8comment', default=1)
    s3_e9_hr = models.IntegerField()
    s3_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s3e9comment', default=1)
    s3_e10_hr = models.IntegerField()
    s3_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='me1s3e10comment', default=1)
    s3_e11_hr = models.IntegerField()
    s3_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='me1s3e11comment', default=1)
    s3_e12_hr = models.IntegerField()
    s3_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='me1s3e12comment', default=1)

    s4_e1_hr = models.IntegerField()
    s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s4e1comment', default=1)

    s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s5e1comment', default=1)
    s5_e2_delay = models.FloatField()
    s5_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s5e2comment', default=1)
    s5_e3_delay = models.FloatField()
    s5_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s5e3comment', default=1)
    s5_e4_delay = models.FloatField()
    s5_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s5e4comment', default=1)

    s6_e1_damp = models.FloatField()
    s6_e1_ramp = models.FloatField(null=True, blank=True)
    s6_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s6e1comment', default=1)
    s6_e2_damp = models.FloatField()
    s6_e2_ramp = models.FloatField(null=True, blank=True)
    s6_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s6e2comment', default=1)
    s6_e3_damp = models.FloatField()
    s6_e3_ramp = models.FloatField(null=True, blank=True)
    s6_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s6e3comment', default=1)

    s7_e1_damp = models.FloatField()
    s7_e1_ramp = models.FloatField(null=True, blank=True)
    s7_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s7e1comment', default=1)
    s7_e2_damp = models.FloatField()
    s7_e2_ramp = models.FloatField(null=True, blank=True)
    s7_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s7e2comment', default=1)
    s7_e3_damp = models.FloatField()
    s7_e3_ramp = models.FloatField(null=True, blank=True)
    s7_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s7e3comment', default=1)
    s7_e4_damp = models.FloatField()
    s7_e4_ramp = models.FloatField(null=True, blank=True)
    s7_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s7e4comment', default=1)
    s7_e5_damp = models.FloatField()
    s7_e5_ramp = models.FloatField(null=True, blank=True)
    s7_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s7e5comment', default=1)

    s8_e1_bdisp = models.FloatField()
    s8_e1_slope = models.FloatField()
    s8_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s8e1comment', default=1)

    s9_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='me1s9e1comment', default=1)

    def __str__(self):
        return 'MonitorECG : ' + str(self.Licence)


class MonitorNIBP_1(models.Model):
    class Meta:
        verbose_name_plural = "Monitor NIBP"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='mn1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='mn1licence')
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='mn1r')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mn1caldev1', default=4)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mn1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mn1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s1_e1_simp = models.IntegerField(default=50)
    s1_e1_nibpp = models.IntegerField()
    s1_e2_simp = models.IntegerField(default=80)
    s1_e2_nibpp = models.IntegerField()
    s1_e3_simp = models.IntegerField(default=120)
    s1_e3_nibpp = models.IntegerField()
    s1_e4_simp = models.IntegerField(default=200)
    s1_e4_nibpp = models.IntegerField()
    s1_e5_simp = models.IntegerField(default=50)
    s1_e5_nibpp = models.IntegerField()
    s1_e6_simp = models.IntegerField(default=80)
    s1_e6_nibpp = models.IntegerField()
    s1_e7_simp = models.IntegerField(default=120)
    s1_e7_nibpp = models.IntegerField()
    s1_e8_simp = models.IntegerField(default=200)
    s1_e8_nibpp = models.IntegerField()

    s2_e1_pr1 = models.CharField(max_length=8)
    s2_e1_pr2 = models.CharField(max_length=8)
    s2_e1_pr3 = models.CharField(max_length=8)
    s2_e2_pr1 = models.CharField(max_length=8)
    s2_e2_pr2 = models.CharField(max_length=8)
    s2_e2_pr3 = models.CharField(max_length=8)
    s2_e3_pr1 = models.CharField(max_length=8)
    s2_e3_pr2 = models.CharField(max_length=8)
    s2_e3_pr3 = models.CharField(max_length=8)
    s2_e4_pr1 = models.CharField(max_length=8)
    s2_e4_pr2 = models.CharField(max_length=8)
    s2_e4_pr3 = models.CharField(max_length=8)
    s2_e5_pr1 = models.CharField(max_length=8)
    s2_e5_pr2 = models.CharField(max_length=8)
    s2_e5_pr3 = models.CharField(max_length=8)
    s2_e6_pr1 = models.CharField(max_length=8)
    s2_e6_pr2 = models.CharField(max_length=8)
    s2_e6_pr3 = models.CharField(max_length=8)

    def __str__(self):
        return 'MonitorNIBP : ' + str(self.Licence)


class AED_1(models.Model):
    class Meta:
        verbose_name_plural = "AED"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='aed1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='aed1licence')
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='aed1r')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='aed1caldev1', default=7)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='aed1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e1comment', default=1)

    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e2comment', default=1)

    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e3comment', default=1)

    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e4comment', default=1)

    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e5comment', default=1)

    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e6comment', default=1)

    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e7comment', default=1)

    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e8comment', default=1)

    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='aed1s0e9comment', default=1)

    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='aed1s0e10comment', default=1)

    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='aed1s0e11comment', default=1)

    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='aed1s0e12comment', default=1)

    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='aed1s0e13comment', default=1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='aed1tt')

    # s1_e1_res = models.FloatField(default=-1)
    # s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s1e1comment', default=2)

    # s2_e1_lc = models.IntegerField(default=-1)
    # s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e1comment', default=2)
    # s2_e2_lc = models.IntegerField(default=-1)
    # s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e2comment', default=2)
    # s2_e3_lc = models.IntegerField(default=-1)
    # s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e3comment', default=2)
    # s2_e4_lc = models.IntegerField(default=-1)
    # s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e4comment', default=2)
    # s2_e5_lc = models.IntegerField(default=-1)
    # s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e5comment', default=2)
    # s2_e6_lc = models.IntegerField(default=-1)
    # s2_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e6comment', default=2)
    # s2_e7_lc = models.IntegerField(default=-1)
    # s2_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s2e7comment', default=2)

    # s3_e1_lc = models.IntegerField(default=-1)
    # s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e1comment', default=2)
    # s3_e2_lc = models.IntegerField(default=-1)
    # s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e2comment', default=2)
    # s3_e3_lc = models.IntegerField(default=-1)
    # s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e3comment', default=2)
    # s3_e4_lc = models.IntegerField(default=-1)
    # s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e4comment', default=2)
    # s3_e5_lc = models.IntegerField(default=-1)
    # s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e5comment', default=2)
    # s3_e6_lc = models.IntegerField(default=-1)
    # s3_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e6comment', default=2)
    # s3_e7_lc = models.IntegerField(default=-1)
    # s3_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s3e7comment', default=2)

    # s4_type = models.ForeignKey(
    #     acc.models.AdTestType1, on_delete=models.CASCADE, related_name='aed1s4_t', default=1)

    # s4_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e1_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e1_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e1comment', default=2)
    # s4_e2_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e2_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e2_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e2_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e2comment', default=2)
    # s4_e3_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e3_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e3_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e3_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e3comment', default=2)
    # s4_e4_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e4_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e4_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e4_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e4comment', default=2)
    # s4_e5_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e5_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e5_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e5_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e5comment', default=2)
    # s4_e6_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e6_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e6_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e6_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e6comment', default=2)
    # s4_e7_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e7_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e7_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e7_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e7comment', default=2)
    # s4_e8_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e8_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e8_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e8_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e8comment', default=2)
    # s4_e9_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e9_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e9_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e9_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s4e9comment', default=2)
    # s4_e10_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e10_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e10_lc3 = models.IntegerField(null=True, blank=True)
    # s4_e10_lc4 = models.IntegerField(null=True, blank=True)
    # s4_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                    related_name='aed1s4e10comment', default=2)

    # s5_type = models.ForeignKey(
    #     acc.models.AdTestType1, on_delete=models.CASCADE, related_name='aed1s5_t', default=1)

    # s5_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e1_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e1_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e1comment', default=2)
    # s5_e2_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e2_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e2_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e2_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e2comment', default=2)
    # s5_e3_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e3_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e3_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e3_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e3comment', default=2)
    # s5_e4_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e4_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e4_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e4_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e4comment', default=2)
    # s5_e5_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e5_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e5_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e5_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e5comment', default=2)
    # s5_e6_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e6_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e6_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e6_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e6comment', default=2)
    # s5_e7_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e7_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e7_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e7_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e7comment', default=2)
    # s5_e8_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e8_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e8_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e8_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e8comment', default=2)
    # s5_e9_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e9_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e9_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e9_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s5e9comment', default=2)
    # s5_e10_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e10_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e10_lc3 = models.IntegerField(null=True, blank=True)
    # s5_e10_lc4 = models.IntegerField(null=True, blank=True)
    # s5_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                    related_name='aed1s5e10comment', default=2)

    # s6_type = models.ForeignKey(
    #     acc.models.AdTestType1, on_delete=models.CASCADE, related_name='aed1s6_t', default=1)

    # s6_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s6_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s6_e1_lc3 = models.IntegerField(null=True, blank=True)
    # s6_e1_lc4 = models.IntegerField(null=True, blank=True)
    # s6_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='aed1s6e1comment', default=2)

    s11_e1_t = models.IntegerField()
    # s11_e2_t = models.IntegerField(null=True, blank=True, default=-1)
    # s11_e3_t = models.IntegerField(null=True, blank=True, default=-1)

    s12_e1_t = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='aed1s12e1comment', default=1)
    s13_e1_e = models.IntegerField()
    s13_e2_e = models.IntegerField()
    s13_e3_e = models.BooleanField()

    def __str__(self):
        return 'AED : ' + str(self.Licence)


class MonitorSafety_1(models.Model):
    class Meta:
        verbose_name_plural = "Monitor Safety"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='msa1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='msa1licence')
    record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='msa1r')
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='msa1caldev1', default=6)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='msa1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='msa1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e1comment', default=1)

    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e2comment', default=1)

    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e3comment', default=1)

    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e4comment', default=1)

    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e5comment', default=1)

    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e6comment', default=1)

    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e7comment', default=1)

    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e8comment', default=1)

    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='msa1s0e9comment', default=1)

    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e10comment', default=1)

    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e11comment', default=1)

    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e12comment', default=1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e13comment', default=1)

    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e14comment', default=1)

    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e15comment', default=1)

    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e16comment', default=1)

    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e17comment', default=1)

    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e18comment', default=1)

    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e19comment', default=1)

    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e20comment', default=1)

    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e21comment', default=1)

    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='msa1s0e22comment', default=1)

    # s1_e1_res = models.IntegerField()
    # s1_e2_res = models.IntegerField()
    # s1_e3_res = models.IntegerField()
    s1_e4_res = models.IntegerField()

    s2_e1_aplc = models.FloatField()
    s2_e1_noaplc = models.FloatField()
    s2_e2_aplc = models.FloatField()
    s2_e2_noaplc = models.FloatField()

    s3_e1_aplc = models.FloatField()
    s3_e1_noaplc = models.FloatField()
    s3_e2_aplc = models.FloatField()
    s3_e2_noaplc = models.FloatField()
    s3_e3_aplc = models.FloatField()
    s3_e3_noaplc = models.FloatField()
    s3_e4_aplc = models.FloatField()
    s3_e4_noaplc = models.FloatField()
    s3_e5_aplc = models.FloatField()
    s3_e5_noaplc = models.FloatField()
    s3_e6_aplc = models.FloatField()
    s3_e6_noaplc = models.FloatField()

    s4_e1_lc = models.FloatField()

    s4_e2_lc = models.FloatField()

    s4_e3_lc = models.FloatField()

    s4_e4_lc = models.FloatField()

    s4_e5_lc = models.FloatField()

    s4_e6_lc = models.FloatField()

    s4_e7_lc = models.FloatField()

    s4_e8_lc = models.FloatField()

    s4_e9_lc = models.FloatField()

    s4_e10_lc = models.FloatField()

    s4_e11_lc = models.FloatField()

    s4_e12_lc = models.FloatField()

    s4_e13_lc = models.FloatField()

    s4_e14_lc = models.FloatField()

    s4_e15_lc = models.FloatField()

    s4_e16_lc = models.FloatField()

    s4_e17_lc = models.FloatField()

    s4_e18_lc = models.FloatField()

    s4_e19_lc = models.FloatField()

    s4_e20_lc = models.FloatField()

    s4_e21_lc = models.FloatField()

    s5_e1_lc = models.FloatField()
    s5_e2_lc = models.FloatField()
    s5_e3_lc = models.FloatField()
    s5_e4_lc = models.FloatField()
    s5_e5_lc = models.FloatField()
    s5_e6_lc = models.FloatField()
    s5_e7_lc = models.FloatField()
    s5_e8_lc = models.FloatField()
    s5_e9_lc = models.FloatField()
    s5_e10_lc = models.FloatField()
    s5_e11_lc = models.FloatField()
    s5_e12_lc = models.FloatField()
    s5_e13_lc = models.FloatField()
    s5_e14_lc = models.FloatField()
    s5_e15_lc = models.FloatField()

    def __str__(self):
        return 'MonitorSafety : ' + str(self.Licence)


class AnesthesiaMachine_1(models.Model):
    class Meta:
        verbose_name_plural = "Anesthesia Machine"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='am1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='am1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='am1caldev1', default=8)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='am1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='am1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='am1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e1comment', default=1)

    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e2comment', default=1)

    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e3comment', default=1)

    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e4comment', default=1)

    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e5comment', default=1)

    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e6comment', default=1)

    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e7comment', default=1)

    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e8comment', default=1)

    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s0e9comment', default=1)

    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e10comment', default=1)

    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e11comment', default=1)

    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e12comment', default=1)

    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e13comment', default=1)

    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e14comment', default=1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e15comment', default=1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e16comment', default=2)

    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e17comment', default=2)

    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e18comment', default=1)

    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e19comment', default=1)

    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e20comment', default=1)

    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e21comment', default=1)

    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e22comment', default=1)

    s0_e23_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e23comment', default=1)

    s0_e24_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e24comment', default=1)

    s0_e25_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e25comment', default=1)

    s0_e26_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e26comment', default=1)

    s0_e27_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e27comment', default=1)

    s0_e28_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e28comment', default=1)

    s0_e29_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e29comment', default=1)

    s0_e30_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e30comment', default=2)

    s0_e31_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s0e31comment', default=1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='am1tt')

    s1_res = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s1e1comment', default=1)
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s1e2comment', default=1)

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s2e1comment', default=1)
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s2e2comment', default=1)
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s2e3comment', default=1)
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s2e4comment', default=1)
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s2e5comment', default=1)

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s3e1comment', default=1)
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s3e2comment', default=1)
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s3e3comment', default=1)
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s3e4comment', default=1)
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='am1s3e5comment', default=1)

    # s4_e1_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e1_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e1comment', default=2)

    # s4_e2_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e2_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e2comment', default=2)
    # s4_e3_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e3_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e3comment', default=2)
    # s4_e4_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e4_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e4comment', default=2)
    # s4_e5_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e5_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e5comment', default=2)
    # s4_e6_dclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e6_aclc = models.IntegerField(null=True, blank=True, default=-1)
    # s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s4e6comment', default=2)

    # s5_e1_cflc = models.IntegerField(null=True, blank=True, default=-1)
    # s5_e1_bflc = models.IntegerField(null=True, blank=True, default=-1)
    # s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='am1s5e1comment', default=2)

    s6_e1_rff = models.IntegerField()
    s6_e1_ffr = models.IntegerField()

    # s7_e1_si1 = models.IntegerField(null=True, blank=True, default=-1)
    # s7_e1_si2 = models.IntegerField(null=True, blank=True, default=-1)
    # s7_e1_si3 = models.IntegerField(null=True, blank=True, default=-1)
    # s7_e1_si4 = models.IntegerField(null=True, blank=True, default=-1)

    s8_e1_status = models.BooleanField(default=False)

    s9_e1 = models.IntegerField()

    s10_e1 = models.IntegerField()

    s11_e1_status = models.BooleanField(default=False)

    s12_e1 = models.FloatField(null=True, blank=True)
    s12_e2 = models.FloatField(null=True, blank=True)
    s12_e3 = models.FloatField(null=True, blank=True)

    s13_me = models.IntegerField(default=10)
    s13_e1_ro2f = models.IntegerField()
    # s13_e1_ro2n2of = models.IntegerField(default=-1)
    s13_e2_ro2f = models.IntegerField()
    # s13_e2_ro2n2of = models.IntegerField(default=-1)
    s13_e3_o2p = models.IntegerField()
    s13_e3_ro2d = models.IntegerField()
    s13_e3_ro2c = models.IntegerField()

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()

    s15_e1 = models.FloatField()
    s15_e2 = models.FloatField()
    s15_e3 = models.FloatField()

    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()

    s17_e03 = models.IntegerField(default=-1)
    s17_e04 = models.IntegerField(default=-1)
    s17_e01 = models.IntegerField(default=-1)
    s17_e02 = models.IntegerField(default=-1)
    s17_e1 = models.IntegerField()
    s17_e2 = models.IntegerField()
    s17_e3 = models.IntegerField(default=-1)
    s17_e4 = models.IntegerField(default=-1)
    s17_e5 = models.FloatField()
    s17_e6 = models.IntegerField()

    s18_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e1comment', default=1)
    s18_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e2comment', default=1)
    s18_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e3comment', default=1)
    s18_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e4comment', default=1)
    s18_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e5comment', default=1)
    s18_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e6comment', default=1)
    s18_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e7comment', default=1)
    s18_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e8comment', default=1)
    s18_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='am1s18e9comment', default=1)
    s18_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                        related_name='am1s18e10comment', default=1)

    # s19_g1_e1 = models.FloatField(default= -1 )
    # s19_g1_e2 = models.FloatField(default= -1 )
    # s19_g1_e3 = models.FloatField(default= -1 )
    # s19_g1_e4 = models.FloatField(default= -1 )
    s19_g2_e1 = models.FloatField()
    s19_g2_e2 = models.FloatField()
    s19_g2_e3 = models.FloatField()
    # s19_g2_e4 = models.FloatField(default= -1)
    # s19_g3_e1 = models.FloatField(default= -1 )
    # s19_g3_e2 = models.FloatField(default= -1 )
    # s19_g3_e3 = models.FloatField(default= -1 )
    # s19_g3_e4 = models.FloatField(default= -1 )
    # s19_g4_e1 = models.FloatField(default= -1 )
    # s19_g4_e2 = models.FloatField(default= -1 )
    # s19_g4_e3 = models.FloatField(default= -1 )
    # s19_g4_e4 = models.FloatField(default= -1 )

    def __str__(self):
        return 'AnesthesiaMachine : ' + str(self.Licence)


class Defibrilator_1(models.Model):
    class Meta:
        verbose_name_plural = "Defibrilator"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='df1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='df1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='df1caldev1', default=7)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='df1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='df1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='df1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e1comment', default=1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e2comment', default=1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e3comment', default=1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e4comment', default=1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e5comment', default=1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e6comment', default=1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e7comment', default=1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e8comment', default=1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s0e9comment', default=1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e10comment', default=1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e11comment', default=1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e12comment', default=1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e13comment', default=1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e14comment', default=1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e15comment', default=1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e16comment', default=2)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e17comment', default=1)
    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e18comment', default=1)
    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e19comment', default=1)
    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e20comment', default=1)
    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e21comment', default=1)
    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s0e22comment', default=1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='df1tt')

    s1_res = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s1e1comment', default=1)

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e1comment', default=1)
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e2comment', default=1)
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e3comment', default=1)
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e4comment', default=1)
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e5comment', default=1)
    s2_e6_lc = models.IntegerField()
    s2_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e6comment', default=1)
    s2_e7_lc = models.IntegerField()
    s2_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s2e7comment', default=1)

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e1comment', default=1)
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e2comment', default=1)
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e3comment', default=1)
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e4comment', default=1)
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e5comment', default=1)
    s3_e6_lc = models.IntegerField()
    s3_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e6comment', default=1)
    s3_e7_lc = models.IntegerField()
    s3_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s3e7comment', default=1)

    s4_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='df1s4_t')

    s4_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e1_lc3 = models.IntegerField(null=True, blank=True)
    s4_e1_lc4 = models.IntegerField(null=True, blank=True)
    s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e1comment', default=1)
    s4_e2_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e2_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e2_lc3 = models.IntegerField(null=True, blank=True)
    s4_e2_lc4 = models.IntegerField(null=True, blank=True)
    s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e2comment', default=1)
    s4_e3_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e3_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e3_lc3 = models.IntegerField(null=True, blank=True)
    s4_e3_lc4 = models.IntegerField(null=True, blank=True)
    s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e3comment', default=1)
    s4_e4_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e4_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e4_lc3 = models.IntegerField(null=True, blank=True)
    s4_e4_lc4 = models.IntegerField(null=True, blank=True)
    s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e4comment', default=1)
    s4_e5_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e5_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e5_lc3 = models.IntegerField(null=True, blank=True)
    s4_e5_lc4 = models.IntegerField(null=True, blank=True)
    s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e5comment', default=1)
    s4_e6_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e6_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e6_lc3 = models.IntegerField(null=True, blank=True)
    s4_e6_lc4 = models.IntegerField(null=True, blank=True)
    s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e6comment', default=1)
    s4_e7_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e7_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e7_lc3 = models.IntegerField(null=True, blank=True)
    s4_e7_lc4 = models.IntegerField(null=True, blank=True)
    s4_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e7comment', default=1)
    s4_e8_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e8_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e8_lc3 = models.IntegerField(null=True, blank=True)
    s4_e8_lc4 = models.IntegerField(null=True, blank=True)
    s4_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e8comment', default=1)
    s4_e9_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e9_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e9_lc3 = models.IntegerField(null=True, blank=True)
    s4_e9_lc4 = models.IntegerField(null=True, blank=True)
    s4_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s4e9comment', default=1)
    s4_e10_lc1 = models.IntegerField(null=True, blank=True)
    # s4_e10_lc2 = models.IntegerField(null=True, blank=True)
    # s4_e10_lc3 = models.IntegerField(null=True, blank=True)
    s4_e10_lc4 = models.IntegerField(null=True, blank=True)
    s4_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s4e10comment', default=1)

    s5_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='df1s5_t')

    s5_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e1_lc3 = models.IntegerField(null=True, blank=True)
    s5_e1_lc4 = models.IntegerField(null=True, blank=True)
    s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e1comment', default=1)
    s5_e2_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e2_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e2_lc3 = models.IntegerField(null=True, blank=True)
    s5_e2_lc4 = models.IntegerField(null=True, blank=True)
    s5_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e2comment', default=1)
    s5_e3_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e3_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e3_lc3 = models.IntegerField(null=True, blank=True)
    s5_e3_lc4 = models.IntegerField(null=True, blank=True)
    s5_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e3comment', default=1)
    s5_e4_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e4_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e4_lc3 = models.IntegerField(null=True, blank=True)
    s5_e4_lc4 = models.IntegerField(null=True, blank=True)
    s5_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e4comment', default=1)
    s5_e5_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e5_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e5_lc3 = models.IntegerField(null=True, blank=True)
    s5_e5_lc4 = models.IntegerField(null=True, blank=True)
    s5_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e5comment', default=1)
    s5_e6_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e6_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e6_lc3 = models.IntegerField(null=True, blank=True)
    s5_e6_lc4 = models.IntegerField(null=True, blank=True)
    s5_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e6comment', default=1)
    s5_e7_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e7_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e7_lc3 = models.IntegerField(null=True, blank=True)
    s5_e7_lc4 = models.IntegerField(null=True, blank=True)
    s5_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e7comment', default=1)
    s5_e8_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e8_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e8_lc3 = models.IntegerField(null=True, blank=True)
    s5_e8_lc4 = models.IntegerField(null=True, blank=True)
    s5_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e8comment', default=1)
    s5_e9_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e9_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e9_lc3 = models.IntegerField(null=True, blank=True)
    s5_e9_lc4 = models.IntegerField(null=True, blank=True)
    s5_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s5e9comment', default=1)
    s5_e10_lc1 = models.IntegerField(null=True, blank=True)
    # s5_e10_lc2 = models.IntegerField(null=True, blank=True)
    # s5_e10_lc3 = models.IntegerField(null=True, blank=True)
    s5_e10_lc4 = models.IntegerField(null=True, blank=True)
    s5_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s5e10comment', default=1)

    s6_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='df1s6_t')

    s6_e1_lc1 = models.IntegerField(null=True, blank=True)
    # s6_e1_lc2 = models.IntegerField(null=True, blank=True)
    # s6_e1_lc3 = models.IntegerField(null=True, blank=True)
    s6_e1_lc4 = models.IntegerField(null=True, blank=True)
    s6_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s6e1comment', default=1)

    s7a_e1_se = models.IntegerField(default=50)
    s7a_e1_es = models.IntegerField(null=True, blank=True)
    s7a_e1_em = models.IntegerField()
    s7a_e1_ec = models.IntegerField(null=True, blank=True)
    s7a_e1_v = models.IntegerField()
    s7a_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ae1comment', default=1)
    s7a_e2_se = models.IntegerField(default=100)
    s7a_e2_es = models.IntegerField(null=True, blank=True)
    s7a_e2_em = models.IntegerField()
    s7a_e2_ec = models.IntegerField(null=True, blank=True)
    s7a_e2_v = models.IntegerField()
    s7a_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ae2comment', default=1)
    s7a_e3_se = models.IntegerField(default=200)
    s7a_e3_es = models.IntegerField(null=True, blank=True)
    s7a_e3_em = models.IntegerField()
    s7a_e3_ec = models.IntegerField(null=True, blank=True)
    s7a_e3_v = models.IntegerField()
    s7a_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ae3comment', default=1)

    # s7b_e1_se = models.IntegerField(default=-1)
    # s7b_e1_es = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e1_em = models.IntegerField(default=-1)
    # s7b_e1_ec = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e1_v = models.IntegerField(default=-1)
    # s7b_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                    related_name='df1s7be1comment', default=2)
    # s7b_e2_se = models.IntegerField(default=-1)
    # s7b_e2_es = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e2_em = models.IntegerField(default=-1)
    # s7b_e2_ec = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e2_v = models.IntegerField(default=-1)
    # s7b_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                    related_name='df1s7be2comment', default=2)
    # s7b_e3_se = models.IntegerField(default=-1)
    # s7b_e3_es = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e3_em = models.IntegerField(default=-1)
    # s7b_e3_ec = models.IntegerField(default=-1, null=True, blank=True)
    # s7b_e3_v = models.IntegerField(default=-1)
    # s7b_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                    related_name='df1s7be3comment', default=2)
    s7c_e1_se = models.IntegerField(default=10)
    s7c_e1_es = models.IntegerField(null=True, blank=True)
    s7c_e1_em = models.IntegerField()
    s7c_e1_ec = models.IntegerField(null=True, blank=True)
    s7c_e1_v = models.IntegerField()
    s7c_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ce1comment', default=1)
    s7c_e2_se = models.IntegerField(default=30)
    s7c_e2_es = models.IntegerField(null=True, blank=True)
    s7c_e2_em = models.IntegerField()
    s7c_e2_ec = models.IntegerField(null=True, blank=True)
    s7c_e2_v = models.IntegerField()
    s7c_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ce2comment', default=1)
    s7c_e3_se = models.IntegerField(default=50)
    s7c_e3_es = models.IntegerField(null=True, blank=True)
    s7c_e3_em = models.IntegerField()
    s7c_e3_ec = models.IntegerField(null=True, blank=True)
    s7c_e3_v = models.IntegerField()
    s7c_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7ce3comment', default=1)

    s7d_e1_en = models.IntegerField()
    s7d_e1_es = models.IntegerField()
    s7d_e1_ec = models.IntegerField()
    s7d_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s7de1comment', default=1)

    s8_e1_en = models.IntegerField()
    s8_e1_em1 = models.IntegerField()
    s8_e1_em2 = models.IntegerField()
    s8_e1_ec = models.IntegerField()
    s8_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s8e1comment', default=1)
    s9_e1_en = models.IntegerField()
    s9_e1_t1 = models.IntegerField()
    s9_e1_tc = models.IntegerField(null=True, blank=True)
    s9_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='df1s9e1comment', default=1)

    s10_minenergy = models.IntegerField(default=200)
    s10_e1_ct = models.IntegerField()
    s10_e1_en = models.IntegerField()
    s10_e1_enl = models.IntegerField()
    s10_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e1comment', default=1)
    s10_e2_ct = models.IntegerField()
    s10_e2_en = models.IntegerField()
    s10_e2_enl = models.IntegerField()
    s10_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e2comment', default=1)
    s10_e3_ct = models.IntegerField()
    s10_e3_en = models.IntegerField()
    s10_e3_enl = models.IntegerField()
    s10_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e3comment', default=1)
    s10_e4_ct = models.IntegerField()
    s10_e4_en = models.IntegerField()
    s10_e4_enl = models.IntegerField()
    s10_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e4comment', default=1)
    s10_e5_ct = models.IntegerField()
    s10_e5_en = models.IntegerField()
    s10_e5_enl = models.IntegerField()
    s10_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e5comment', default=1)
    s10_e6_ct = models.IntegerField()
    s10_e6_en = models.IntegerField()
    s10_e6_enl = models.IntegerField()
    s10_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e6comment', default=1)
    s10_e7_ct = models.IntegerField()
    s10_e7_en = models.IntegerField()
    s10_e7_enl = models.IntegerField()
    s10_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e7comment', default=1)
    s10_e8_ct = models.IntegerField()
    s10_e8_en = models.IntegerField()
    s10_e8_enl = models.IntegerField()
    s10_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e8comment', default=1)
    s10_e9_ct = models.IntegerField()
    s10_e9_en = models.IntegerField()
    s10_e9_enl = models.IntegerField()
    s10_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s10e9comment', default=1)
    s10_e10_ct = models.IntegerField()
    s10_e10_en = models.IntegerField()
    s10_e10_enl = models.IntegerField()
    s10_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                        related_name='df1s10e10comment', default=1)

    s11_e1_en = models.IntegerField(default=50)
    s11_e1_t = models.IntegerField()
    s11_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s11e1comment', default=1)

    s12_e1_en = models.IntegerField()
    s12_e1_cc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s12e1comment', default=1)
    s12_e2_en = models.IntegerField()
    s12_e2_cc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s12e2comment', default=1)
    s12_e3_en = models.IntegerField()
    s12_e3_cc = models.IntegerField()
    s12_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='df1s12e3comment', default=1)

    def __str__(self):
        return 'Defibrilator : ' + str(self.Licence)


class ECG_1(models.Model):
    class Meta:
        verbose_name_plural = "ElectroCardioGraph"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='e1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='e1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)
    

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='e1caldev1', default=5)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='e1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='e1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='e1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    
    s1_e1_damp = models.FloatField()
    s1_e1_ramp = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s1e1comment', default=1)
    s1_e2_damp = models.FloatField()
    s1_e2_ramp = models.FloatField()
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s1e2comment', default=1)
    s1_e3_damp = models.FloatField()
    s1_e3_ramp = models.FloatField()
    s1_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s1e3comment', default=1)

    s2_e1_nspeak = models.FloatField()
    s2_e2_nspeak = models.FloatField()
    s2_e3_nspeak = models.FloatField()
    s2_e4_nspeak = models.FloatField()
    s2_e5_nspeak = models.FloatField()
    s2_e6_nspeak = models.FloatField()

    s3_e1_mr = models.FloatField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s3e1comment', default=1)

    s4_e1_mr = models.FloatField()
    s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e1comment', default=1)
    s4_e2_mr = models.FloatField()
    s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e2comment', default=1)
    s4_e3_mr = models.FloatField()
    s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e3comment', default=1)
    s4_e4_mr = models.FloatField()
    s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e4comment', default=1)
    s4_e5_mr = models.FloatField()
    s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e5comment', default=1)
    s4_e6_mr = models.FloatField()
    s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s4e6comment', default=1)

    s5_e1_mr = models.FloatField()
    s5_e2_mr = models.FloatField()
    s5_e3_mr = models.FloatField()
    s5_e4_mr = models.FloatField()
    s5_e5_mr = models.FloatField()
    s5_e6_mr = models.FloatField()
    s5_e7_mr = models.FloatField()
    s5_e8_mr = models.FloatField()
    s5_e9_mr = models.FloatField()
    s5_e10_mr = models.FloatField()
    s5_e11_mr = models.FloatField()
    s5_e12_mr = models.FloatField()

    s6_e1_ramp = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s6e1comment', default=1)
    s6_e2_ramp = models.FloatField()
    s6_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s6e2comment', default=1)
    s6_e3_ramp = models.FloatField()
    s6_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s6e3comment', default=1)

    s7_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e1comment', default=1)

    s7_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e2comment', default=1)

    s7_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e3comment', default=1)

    s7_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e4comment', default=1)

    s7_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e5comment', default=1)

    s7_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e6comment', default=1)

    s7_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e7comment', default=1)

    s7_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='e1s7e8comment', default=1)

    s11_e1_acc = models.ForeignKey(acc.models.Accessory, on_delete=models.PROTECT, related_name='e1s11e1accessory',
                                   default=1)  # N/A
    s11_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s11e1comment', default=2)

    s11_e2_acc = models.ForeignKey(acc.models.Accessory, on_delete=models.PROTECT, related_name='e1s11e2accessory',
                                   default=1)  # N/A
    s11_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s11e2comment', default=2)

    s11_e3_acc = models.ForeignKey(acc.models.Accessory, on_delete=models.PROTECT, related_name='e1s11e3accessory',
                                   default=1)  # N/A
    s11_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s11e3comment', default=2)

    s11_e4_acc = models.ForeignKey(acc.models.Accessory, on_delete=models.PROTECT, related_name='e1s11e4accessory',
                                   default=1)  # N/A
    s11_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s11e4comment', default=2)

    s11_e5_acc = models.ForeignKey(acc.models.Accessory, on_delete=models.PROTECT, related_name='e1s11e5accessory',
                                   default=1)  # N/A
    s11_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s11e5comment', default=2)

    s12_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s12e1comment', default=1)
    s12_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s12e2comment', default=1)
    s12_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s12e3comment', default=1)
    s12_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s12e4comment', default=1)

    s13_e1_va = models.FloatField()
    s13_e1_watt = models.FloatField()
    s13_e1_v = models.FloatField()
    s13_e1_a = models.FloatField()

    s14_e1_type = models.BooleanField()
    s14_e1_er = models.FloatField()
    s14_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s14e1comment', default=1)

    s15_e1_aplc = models.FloatField(null=True, blank=True)
    s15_e1_noaplc = models.FloatField(null=True, blank=True)
    s15_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s15e1comment', default=1)
    s15_e2_aplc = models.FloatField(null=True, blank=True)
    s15_e2_noaplc = models.FloatField(null=True, blank=True)
    s15_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s15e2comment', default=1)

    s16_e1_aplc = models.FloatField(null=True, blank=True)
    s16_e1_noaplc = models.FloatField(null=True, blank=True)
    s16_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s16e1comment', default=1)
    s16_e2_aplc = models.FloatField(null=True, blank=True)
    s16_e2_noaplc = models.FloatField(null=True, blank=True)
    s16_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='e1s16e2comment', default=1)

    s17_e1_plc = models.IntegerField()
    s17_e2_plc = models.IntegerField()
    s17_e3_plc = models.IntegerField()
    s17_e4_plc = models.IntegerField()
    s17_e5_plc = models.IntegerField()
    s17_e6_plc = models.IntegerField()
    s17_e7_plc = models.IntegerField()
    s17_e8_plc = models.IntegerField()
    s17_e9_plc = models.IntegerField()
    s17_e10_plc = models.IntegerField()
    s17_e11_plc = models.IntegerField()
    s17_e12_plc = models.IntegerField()

    s18_e1_pac = models.IntegerField()
    s18_e2_pac = models.IntegerField()
    s18_e3_pac = models.IntegerField()
    s18_e4_pac = models.IntegerField()

    def __str__(self):
        return 'ECG : ' + str(self.Licence)


class FlowMeter_1(models.Model):
    class Meta:
        verbose_name_plural = "Flow Meter"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='fm1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='fm1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='fm1caldev1', default=8)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()

    s1_e1_rlpm = models.FloatField()
    s1_e2_rlpm = models.FloatField()
    s1_e3_rlpm = models.FloatField()
    s1_e4_rlpm = models.FloatField()
    s1_e5_rlpm = models.FloatField()
    s1_e6_rlpm = models.FloatField()

    def __str__(self):
        return 'FlowMeter : ' + str(self.Licence)


class InfusionPump_1(models.Model):
    class Meta:
        verbose_name_plural = "Infusion Pump"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ip1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='ip1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ip1caldev1', default=11)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ip1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ip1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ip1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e1comment', default = 1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e2comment', default = 1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e3comment', default = 1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e4comment', default = 1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e5comment', default = 1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e6comment', default = 1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e7comment', default = 1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e8comment', default = 1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s0e9comment', default = 1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e10comment', default = 1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e11comment', default = 1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e12comment', default = 1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e13comment', default = 1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e14comment', default = 1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e15comment', default = 1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e16comment', default = 1)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e17comment', default = 1)
    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e18comment', default = 1)
    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e19comment', default = 1)
    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e20comment', default = 1)
    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e21comment', default = 1)
    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e22comment', default = 1)
    s0_e23_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ip1s0e23comment', default = 1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='ip1tt')

    s1_res = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s1e1comment', default = 1)
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s1e2comment', default = 1)

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s2e1comment', default = 1)
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s2e2comment', default = 1)
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s2e3comment', default = 1)
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s2e4comment', default = 1)
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s2e5comment', default = 1)

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s3e1comment', default = 1)
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s3e2comment', default = 1)
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s3e3comment', default = 1)
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s3e4comment', default = 1)
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s3e5comment', default = 1)

    # s4_e1_dclc = models.IntegerField(default=-1)
    # s4_e1_aclc = models.IntegerField(default=-1)
    # s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e1comment')

    # s4_e2_dclc = models.IntegerField(default=-1)
    # s4_e2_aclc = models.IntegerField(default=-1)
    # s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e2comment')
    # s4_e3_dclc = models.IntegerField(default=-1)
    # s4_e3_aclc = models.IntegerField(default=-1)
    # s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e3comment')
    # s4_e4_dclc = models.IntegerField(default=-1)
    # s4_e4_aclc = models.IntegerField(default=-1)
    # s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e4comment')
    # s4_e5_dclc = models.IntegerField(default=-1)
    # s4_e5_aclc = models.IntegerField(default=-1)
    # s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e5comment')
    # s4_e6_dclc = models.IntegerField(default=-1)
    # s4_e6_aclc = models.IntegerField(default=-1)
    # s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ip1s4e6comment')

    s5_e1_cflc = models.IntegerField(null=True, blank=True)
    s5_e1_bflc = models.IntegerField(null=True, blank=True)
    s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ip1s5e1comment', default = 1)

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()

    s7_e2_mmf = models.IntegerField()

    s8_e1_status = models.BooleanField(default=False)

    def __str__(self):
        return 'InfusionPump : ' + str(self.Licence)


class ManoMeter_1(models.Model):
    class Meta:
        verbose_name_plural = "ManoMeter"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='mm1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='mm1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mm1caldev1', default=4)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mm1caldev2', default=2)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='mm1caldev3', default=3)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e1comment', default=1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e2comment', default=1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e3comment', default=1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e4comment', default=1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e5comment', default=1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e6comment', default=1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e7comment', default=1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e8comment', default=1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s0e9comment', default=1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e10comment', default=1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e11comment', default=1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e12comment', default=1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e13comment', default=1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e14comment', default=1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='mm1s0e15comment', default=1)

    s1_e1_r = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='mm1s1e1comment', default=1)

    s2_e1_sp = models.IntegerField(default=0)
    s2_e1_np = models.IntegerField()
    s2_e2_sp = models.IntegerField(default=60)
    s2_e2_np = models.IntegerField()
    s2_e3_sp = models.IntegerField(default=120)
    s2_e3_np = models.IntegerField()
    s2_e4_sp = models.IntegerField(default=200)
    s2_e4_np = models.IntegerField()

    def __str__(self):
        return 'manometer : ' + str(self.Licence)


class Spo2_1(models.Model):
    class Meta:
        verbose_name_plural = "PulseOxyMeter"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='sp1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='sp1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='sp1caldev1', default=1)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='sp1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='sp1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='sp1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

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

    s3_e1_accessory = models.ForeignKey(
        acc.models.Accessory, on_delete=models.PROTECT, related_name='sp1s3e1accessory')
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s3e1comment')

    s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s4e1comment')
    s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s4e2comment')
    s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s4e3comment')
    s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s4e4comment')

    s5_e1_va = models.FloatField()
    s5_e1_watt = models.FloatField()
    s5_e1_v = models.FloatField()
    s5_e1_a = models.FloatField()

    s6_e1_type = models.BooleanField()
    s6_e1_er = models.FloatField()
    s6_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s6e1comment')

    s7_e1_aplc = models.IntegerField(null=True, blank=True)
    s7_e1_noaplc = models.IntegerField(null=True, blank=True)
    s7_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s7e1comment')
    s7_e2_aplc = models.IntegerField(null=True, blank=True)
    s7_e2_noaplc = models.IntegerField(null=True, blank=True)
    s7_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='sp1s7e2comment')

    

    def __str__(self):
        return 'spo2 : ' + str(self.Licence)


class Suction_1(models.Model):
    class Meta:
        verbose_name_plural = "Suction"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='su1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='su1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='su1caldev1', default=8)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='su1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='su1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='su1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e1comment', default=1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e2comment', default=1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e3comment', default=1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e4comment', default=1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e5comment', default=1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e6comment', default=1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e7comment', default=1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e8comment', default=1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='su1s0e9comment', default=1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e10comment', default=1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e11comment', default=1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e12comment', default=1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e13comment', default=1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e14comment', default=1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e15comment', default=1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e16comment', default=1)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e17comment', default=1)
    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e18comment', default=1)
    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e19comment', default=1)
    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e20comment', default=1)
    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e21comment', default=1)
    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e22comment', default=1)
    s0_e23_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='su1s0e23comment', default=1)
    # TODO permisible error
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
        return 'Suction : ' + str(self.Licence)


class SyringePump_1(models.Model):
    class Meta:
        verbose_name_plural = "Syringe Pump"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='spmp1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='spmp1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='spmp1caldev1', default=11)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='spmp1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='spmp1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='spmp1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e1comment', default=1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e2comment', default=1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e3comment', default=1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e4comment', default=1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e5comment', default=1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e6comment', default=1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e7comment', default=1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e8comment', default=1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s0e9comment', default=1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e10comment', default=1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e11comment', default=1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e12comment', default=2)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e13comment', default=2)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e14comment', default=1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e15comment', default=1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e16comment', default=1)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e17comment', default=1)
    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e18comment', default=1)
    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e19comment', default=1)
    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e20comment', default=1)
    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e21comment', default=2)
    s0_e22_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e22comment', default=1)
    s0_e23_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='spmp1s0e23comment', default=1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='spmp1tt')

    s1_res = models.FloatField()
    s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s1e1comment', default=2)
    s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s1e2comment', default=2)

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s2e1comment', default=1)
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s2e2comment', default=1)
    s2_e3_lc = models.IntegerField()
    s2_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s2e3comment', default=1)
    s2_e4_lc = models.IntegerField()
    s2_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s2e4comment', default=1)
    s2_e5_lc = models.IntegerField()
    s2_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s2e5comment', default=1)

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s3e1comment', default=1)
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s3e2comment', default=1)
    s3_e3_lc = models.IntegerField()
    s3_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s3e3comment', default=1)
    s3_e4_lc = models.IntegerField()
    s3_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s3e4comment', default=1)
    s3_e5_lc = models.IntegerField()
    s3_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s3e5comment', default=1)

    # s4_e1_dclc = models.IntegerField(default=-1)
    # s4_e1_aclc = models.IntegerField(default=-1)
    # s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e1comment', default=2)

    # s4_e2_dclc = models.IntegerField(default=-1)
    # s4_e2_aclc = models.IntegerField(default=-1)
    # s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e2comment', default=2)
    # s4_e3_dclc = models.IntegerField(default=-1)
    # s4_e3_aclc = models.IntegerField(default=-1)
    # s4_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e3comment', default=2)
    # s4_e4_dclc = models.IntegerField(default=-1)
    # s4_e4_aclc = models.IntegerField(default=-1)
    # s4_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e4comment', default=2)
    # s4_e5_dclc = models.IntegerField(default=-1)
    # s4_e5_aclc = models.IntegerField(default=-1)
    # s4_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e5comment', default=2)
    # s4_e6_dclc = models.IntegerField(default=-1)
    # s4_e6_aclc = models.IntegerField(default=-1)
    # s4_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='spmp1s4e6comment', default=2)

    s5_e1_cflc = models.IntegerField(null=True, blank=True)
    s5_e1_bflc = models.IntegerField(null=True, blank=True)
    s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='spmp1s5e1comment', default=1)

    s6_e1_mf = models.IntegerField()
    s6_e2_mf = models.IntegerField()

    s7_e1_mmf = models.IntegerField()
    s7_e2_mmf = models.IntegerField()

    # s8_e1_status = models.BooleanField(default=False)

    def __str__(self):
        return 'SyringePump : ' + str(self.Licence)


class ElectroCauter_1(models.Model):
    class Meta:
        verbose_name_plural = "ElectroCauter"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ec1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='ec1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ec1caldev1', default=9)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ec1caldev2', default=10)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ec1caldev3', default=6)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ec1caldev4', default=2)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()
    cal_dev5 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ec1caldev5', default=3)
    cal_dev_5_cd = models.DateField()
    cal_dev_5_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e1comment', default = 1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e2comment', default = 1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e3comment', default = 1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e4comment', default = 1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e5comment', default = 1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e6comment', default = 1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e7comment', default = 1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e8comment', default = 1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ec1s0e9comment', default = 1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e10comment', default = 1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e11comment', default = 1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e12comment', default = 1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e13comment', default = 1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e14comment', default = 1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e15comment', default = 1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e16comment', default = 2)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s0e17comment', default = 1)

    # s1_res = models.FloatField(default=-1)

    s2_e1 = models.FloatField()
    s2_e2 = models.FloatField()

    s3a_e1_1 = models.FloatField()
    s3a_e1_s = models.FloatField()
    s3a_e1_m = models.FloatField()
    s3a_e2_1 = models.FloatField()
    s3a_e2_s = models.FloatField()
    s3a_e2_m = models.FloatField()
    s3a_e3_1 = models.FloatField()
    s3a_e3_s = models.FloatField()
    s3a_e3_m = models.FloatField()
    # s3a_e4_1 = models.FloatField(default=-1)
    # s3a_e4_s = models.FloatField(default=-1)
    # s3a_e4_m = models.FloatField(default=-1)
    # s3a_e5_1 = models.FloatField(default=-1)
    # s3a_e5_s = models.FloatField(default=-1)
    # s3a_e5_m = models.FloatField(default=-1)
    # s3a_e6_1 = models.FloatField(default=-1)
    # s3a_e6_s = models.FloatField(default=-1)
    # s3a_e6_m = models.FloatField(default=-1)
    # s3a_e7_1 = models.FloatField(default=-1)
    # s3a_e7_s = models.FloatField(default=-1)
    # s3a_e7_m = models.FloatField(default=-1)

    s3b_e1_1 = models.FloatField()
    s3b_e1_s = models.FloatField()
    s3b_e1_m = models.FloatField()
    s3b_e2_1 = models.FloatField()
    s3b_e2_s = models.FloatField()
    s3b_e2_m = models.FloatField()
    s3b_e3_1 = models.FloatField()
    s3b_e3_s = models.FloatField()
    s3b_e3_m = models.FloatField()
    # s3b_e4_1 = models.FloatField(default=-1)
    # s3b_e4_s = models.FloatField(default=-1)
    # s3b_e4_m = models.FloatField(default=-1)
    # s3b_e5_1 = models.FloatField(default=-1)
    # s3b_e5_s = models.FloatField(default=-1)
    # s3b_e5_m = models.FloatField(default=-1)
    # s3b_e6_1 = models.FloatField(default=-1)
    # s3b_e6_s = models.FloatField(default=-1)
    # s3b_e6_m = models.FloatField(default=-1)
    # s3b_e7_1 = models.FloatField(default=-1)
    # s3b_e7_s = models.FloatField(default=-1)
    # s3b_e7_m = models.FloatField(default=-1)

    s3c_e1_1 = models.FloatField()
    s3c_e1_s = models.FloatField()
    s3c_e1_m = models.FloatField()
    s3c_e2_1 = models.FloatField()
    s3c_e2_s = models.FloatField()
    s3c_e2_m = models.FloatField()
    s3c_e3_1 = models.FloatField()
    s3c_e3_s = models.FloatField()
    s3c_e3_m = models.FloatField()
    # s3c_e4_1 = models.FloatField(default=-1)
    # s3c_e4_s = models.FloatField(default=-1)
    # s3c_e4_m = models.FloatField(default=-1)
    # s3c_e5_1 = models.FloatField(default=-1)
    # s3c_e5_s = models.FloatField(default=-1)
    # s3c_e5_m = models.FloatField(default=-1)
    # s3c_e6_1 = models.FloatField(default=-1)
    # s3c_e6_s = models.FloatField(default=-1)
    # s3c_e6_m = models.FloatField(default=-1)
    # s3c_e7_1 = models.FloatField(default=-1)
    # s3c_e7_s = models.FloatField(default=-1)
    # s3c_e7_m = models.FloatField(default=-1)

    s3d_e1_1 = models.FloatField()
    s3d_e1_s = models.FloatField()
    s3d_e1_m = models.FloatField()
    s3d_e2_1 = models.FloatField()
    s3d_e2_s = models.FloatField()
    s3d_e2_m = models.FloatField()
    s3d_e3_1 = models.FloatField()
    s3d_e3_s = models.FloatField()
    s3d_e3_m = models.FloatField()
    # s3d_e4_1 = models.FloatField(default=-1)
    # s3d_e4_s = models.FloatField(default=-1)
    # s3d_e4_m = models.FloatField(default=-1)
    # s3d_e5_1 = models.FloatField(default=-1)
    # s3d_e5_s = models.FloatField(default=-1)
    # s3d_e5_m = models.FloatField(default=-1)
    # s3d_e6_1 = models.FloatField(default=-1)
    # s3d_e6_s = models.FloatField(default=-1)
    # s3d_e6_m = models.FloatField(default=-1)
    # s3d_e7_1 = models.FloatField(default=-1)
    # s3d_e7_s = models.FloatField(default=-1)
    # s3d_e7_m = models.FloatField(default=-1)

    s3e_e1_1 = models.FloatField()
    s3e_e1_s = models.FloatField()
    s3e_e1_m = models.FloatField()
    s3e_e2_1 = models.FloatField()
    s3e_e2_s = models.FloatField()
    s3e_e2_m = models.FloatField()
    s3e_e3_1 = models.FloatField()
    s3e_e3_s = models.FloatField()
    s3e_e3_m = models.FloatField()
    # s3e_e4_1 = models.FloatField(default=-1)
    # s3e_e4_s = models.FloatField(default=-1)
    # s3e_e4_m = models.FloatField(default=-1)
    # s3e_e5_1 = models.FloatField(default=-1)
    # s3e_e5_s = models.FloatField(default=-1)
    # s3e_e5_m = models.FloatField(default=-1)
    # s3e_e6_1 = models.FloatField(default=-1)
    # s3e_e6_s = models.FloatField(default=-1)
    # s3e_e6_m = models.FloatField(default=-1)
    # s3e_e7_1 = models.FloatField(default=-1)
    # s3e_e7_s = models.FloatField(default=-1)
    # s3e_e7_m = models.FloatField(default=-1)

    # s3f_e1_1 = models.FloatField(default=-1)
    # s3f_e1_s = models.FloatField(default=-1)
    # s3f_e1_m = models.FloatField(default=-1)
    # s3f_e2_1 = models.FloatField(default=-1)
    # s3f_e2_s = models.FloatField(default=-1)
    # s3f_e2_m = models.FloatField(default=-1)
    # s3f_e3_1 = models.FloatField(default=-1)
    # s3f_e3_s = models.FloatField(default=-1)
    # s3f_e3_m = models.FloatField(default=-1)
    # s3f_e4_1 = models.FloatField(default=-1)
    # s3f_e4_s = models.FloatField(default=-1)
    # s3f_e4_m = models.FloatField(default=-1)
    # s3f_e5_1 = models.FloatField(default=-1)
    # s3f_e5_s = models.FloatField(default=-1)
    # s3f_e5_m = models.FloatField(default=-1)
    # s3f_e6_1 = models.FloatField(default=-1)
    # s3f_e6_s = models.FloatField(default=-1)
    # s3f_e6_m = models.FloatField(default=-1)
    # s3f_e7_1 = models.FloatField(default=-1)
    # s3f_e7_s = models.FloatField(default=-1)
    # s3f_e7_m = models.FloatField(default=-1)

    # s4a_e1 = models.FloatField(default=-1)
    # s4a_e2 = models.FloatField(default=-1)
    # s4a_e3 = models.FloatField(default=-1)

    # s4b_e1 = models.FloatField(default=-1)
    # s4b_e2 = models.FloatField(default=-1)
    # s4b_e3 = models.FloatField(default=-1)

    s4c_e1 = models.FloatField()
    s4c_e2 = models.FloatField()
    s4c_e3 = models.FloatField()

    s4d_e1 = models.FloatField()
    s4d_e2 = models.FloatField()
    s4d_e3 = models.FloatField()

    s4e_e1 = models.FloatField()
    s4e_e2 = models.FloatField()
    s4e_e3 = models.FloatField()

    s4f_e1 = models.FloatField()
    s4f_e2 = models.FloatField()
    s4f_e3 = models.FloatField()

    s4g_e1 = models.FloatField()
    s4g_e1_p2000 = models.FloatField()
    s4g_e2 = models.FloatField()
    s4g_e2_p2000 = models.FloatField()

    # s4g_e3 = models.FloatField(default=-1)

    # s4h_e1 = models.FloatField(default=-1)
    # s4h_e2 = models.FloatField(default=-1)
    # s4h_e3 = models.FloatField(default=-1)

    # s4i_e1 = models.FloatField(default=-1)
    # s4i_e2 = models.FloatField(default=-1)
    # s4i_e3 = models.FloatField(default=-1)

    # s4j_e1 = models.FloatField(default=-1)
    # s4j_e2 = models.FloatField(default=-1)
    # s4j_e3 = models.FloatField(default=-1)

    # s4k_e1 = models.FloatField(default=-1)
    # s4k_e2 = models.FloatField(default=-1)
    # s4k_e3 = models.FloatField(default=-1)

    # s4l_e1 = models.FloatField(default=-1)
    # s4l_e2 = models.FloatField(default=-1)
    # s4l_e3 = models.FloatField(default=-1)

    s4m_e1 = models.FloatField()
    s4m_e2 = models.FloatField()
    # s4m_e3 = models.FloatField(default=-1)

    s4n_e1 = models.FloatField()
    s4n_e2 = models.FloatField()
    # s4n_e3 = models.FloatField(default=-1)

    # s4o_e1 = models.FloatField(default=-1)
    # s4o_e2 = models.FloatField(default=-1)
    # s4o_e3 = models.FloatField(default=-1)

    # s4p_e1 = models.FloatField(default=-1)
    # s4p_e2 = models.FloatField(default=-1)
    # s4p_e3 = models.FloatField(default=-1)

    # s4q_e1 = models.FloatField(default=-1)
    # s4q_e2 = models.FloatField(default=-1)
    # s4q_e3 = models.FloatField(default=-1)

    # s4r_e1 = models.FloatField(default=-1)
    # s4r_e2 = models.FloatField(default=-1)
    # s4r_e3 = models.FloatField(default=-1)

    s5a_e1 = models.FloatField()
    s5a_e2 = models.FloatField()
    # s5a_e3 = models.FloatField(default=-1)

    s5b_e1 = models.FloatField()
    s5b_e2 = models.FloatField()
    # s5b_e3 = models.FloatField(default=-1)

    # s5c_e1 = models.FloatField(default=-1)
    # s5c_e2 = models.FloatField(default=-1)
    # s5c_e3 = models.FloatField(default=-1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='ec1tt')

    s11_e1_res = models.FloatField()
    s11_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s11e1comment', default = 1)
    s11_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s11e2comment', default = 1)

    s12_e1_lc = models.IntegerField()
    s12_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s12e1comment', default = 1)
    s12_e2_lc = models.IntegerField()
    s12_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s12e2comment', default = 1)

    s13_e1_lc = models.IntegerField()
    s13_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s13e1comment', default = 1)
    s13_e2_lc = models.IntegerField()
    s13_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s13e2comment', default = 1)

    s14_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='ec1s14_t')

    s14_e1_lc1 = models.IntegerField(null=True, blank=True)
    s14_e1_lc2 = models.IntegerField(null=True, blank=True)
    s14_e1_lc3 = models.IntegerField(null=True, blank=True)
    s14_e1_lc4 = models.IntegerField(null=True, blank=True)
    s14_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s14e1comment', default = 1)
    s14_e2_lc1 = models.IntegerField(null=True, blank=True)
    s14_e2_lc2 = models.IntegerField(null=True, blank=True)
    s14_e2_lc3 = models.IntegerField(null=True, blank=True)
    s14_e2_lc4 = models.IntegerField(null=True, blank=True)
    s14_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s14e2comment', default = 1)

    s15_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='ec1s15_t')

    s15_e1_lc1 = models.IntegerField(null=True, blank=True)
    s15_e1_lc2 = models.IntegerField(null=True, blank=True)
    s15_e1_lc3 = models.IntegerField(null=True, blank=True)
    s15_e1_lc4 = models.IntegerField(null=True, blank=True)
    s15_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s15e1comment', default = 1)
    s15_e2_lc1 = models.IntegerField(null=True, blank=True)
    s15_e2_lc2 = models.IntegerField(null=True, blank=True)
    s15_e2_lc3 = models.IntegerField(null=True, blank=True)
    s15_e2_lc4 = models.IntegerField(null=True, blank=True)
    s15_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s15e2comment', default = 1)

    s16_type = models.ForeignKey(
        acc.models.AdTestType1, on_delete=models.CASCADE, related_name='ec1s16_t')

    s16_e1_lc1 = models.IntegerField(null=True, blank=True)
    s16_e1_lc2 = models.IntegerField(null=True, blank=True)
    s16_e1_lc3 = models.IntegerField(null=True, blank=True)
    s16_e1_lc4 = models.IntegerField(null=True, blank=True)
    s16_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ec1s16e1comment', default = 1)

    se_e1_title = models.CharField(max_length=30, null=True, blank=True)
    se_e1_comment = models.CharField(max_length=100, null=True, blank=True)
    se_e2_title = models.CharField(max_length=30, null=True, blank=True)
    se_e2_comment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'electrocouter : ' + str(self.Licence)


class Ventilator_1(models.Model):
    class Meta:
        verbose_name_plural = "Ventilator"
    is_recal = models.BooleanField(default=False)
    ref_record = models.ForeignKey(
        acc.models.Record, on_delete=models.CASCADE, related_name='ven1rr')

    device = models.ForeignKey(acc.models.AllDevice, on_delete=models.PROTECT)
    has_pdf = models.BooleanField(default=False)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(
        acc.models.AdAzStatus, on_delete=models.PROTECT)
    licence = models.ForeignKey(
        acc.models.Licence, on_delete=models.CASCADE, related_name='ven1licence')
    record = models.ForeignKey(acc.models.Record, on_delete=models.CASCADE)
    totalcomment = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    humidity = models.IntegerField(default=45)
    temp = models.IntegerField(default=25)

    # cd = calibration date xd = expire date
    cal_dev1 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ven1caldev1', default=8)
    cal_dev_1_cd = models.DateField()
    cal_dev_1_xd = models.DateField()
    cal_dev2 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ven1caldev2', default=6)
    cal_dev_2_cd = models.DateField()
    cal_dev_2_xd = models.DateField()
    cal_dev3 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ven1caldev3', default=2)
    cal_dev_3_cd = models.DateField()
    cal_dev_3_xd = models.DateField()
    cal_dev4 = models.ForeignKey(
        acc.models.CalDevice, on_delete=models.PROTECT, related_name='ven1caldev4', default=3)
    cal_dev_4_cd = models.DateField()
    cal_dev_4_xd = models.DateField()

    s0_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e1comment', default = 1)
    s0_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e2comment', default = 1)
    s0_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e3comment', default = 1)
    s0_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e4comment', default = 1)
    s0_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e5comment', default = 1)
    s0_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e6comment', default = 1)
    s0_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e7comment', default = 1)
    s0_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e8comment', default = 1)
    s0_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s0e9comment', default = 1)
    s0_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e10comment', default = 1)
    s0_e11_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e11comment', default = 1)
    s0_e12_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e12comment', default = 1)
    s0_e13_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e13comment', default = 1)
    s0_e14_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e14comment', default = 1)
    s0_e15_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e15comment', default = 1)
    s0_e16_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e16comment', default = 1)
    s0_e17_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e17comment', default = 1)
    s0_e18_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e18comment', default = 1)
    s0_e19_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e19comment', default = 1)
    s0_e20_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e20comment', default = 1)
    s0_e21_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s0e21comment', default = 1)

    test_type = models.ForeignKey(
        acc.models.AdTestType, on_delete=models.CASCADE, related_name='ven1tt')

    # s1_res = models.FloatField(default=-1)
    # s1_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ven1s1e1comment')
    # s1_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ven1s1e2comment')

    s2_e1_lc = models.IntegerField()
    s2_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s2e1comment', default = 1)
    s2_e2_lc = models.IntegerField()
    s2_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s2e2comment', default = 1)

    s3_e1_lc = models.IntegerField()
    s3_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s3e1comment', default = 1)
    s3_e2_lc = models.IntegerField()
    s3_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                      related_name='ven1s3e2comment', default = 1)
    # s4_type = models.ForeignKey(acc.models.AdTestType1, on_delete=models.CASCADE, related_name='ven1s4_t')

    # s4_e1_lcac = models.IntegerField(default=-1)
    # s4_e1_lcdc = models.IntegerField(default=-1)
    # s4_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ven1s4e1comment')
    # s4_e2_lcac = models.IntegerField(default=-1)
    # s4_e2_lcdc = models.IntegerField(default=-1)
    # s4_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ven1s4e2comment')

    # s5_type = models.ForeignKey(acc.models.AdTestType1, on_delete=models.CASCADE, related_name='ven1s5_t')

    # s5_e1_lcbf = models.IntegerField(default=-1)
    # s5_e1_lccf = models.IntegerField(default=-1)
    # s5_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
    #                                   related_name='ven1s5e1comment')

    # s6_e1_rff = models.IntegerField(default=-1)
    s6_e1_ffr = models.IntegerField()

    # s7_e1_si1 = models.IntegerField(default=-1)
    # s7_e1_si2 = models.IntegerField(default=-1)
    # s7_e1_si3 = models.IntegerField(default=-1)
    # s7_e1_si4 = models.IntegerField(default=-1)

    s8_e1_status = models.BooleanField(default=False)

    # s9_e1 = models.IntegerField(default=-1)

    # s10_e1 = models.IntegerField(default=-1)

    # s11_e1_status = models.BooleanField(default=False)

    # s12_e1_o2 = models.IntegerField(default=-1)
    # s12_e1_o2n2o = models.IntegerField(default=-1)

    # s13_e1 = models.IntegerField(default=-1)
    # s13_e2 = models.IntegerField(default=-1)

    s14_e1 = models.IntegerField()
    s14_e2 = models.IntegerField()
    s14_e3 = models.IntegerField()

    s15_e1 = models.IntegerField()
    s15_e2 = models.IntegerField()

    s16_1e1 = models.IntegerField(default=-1)
    s16_1e2 = models.IntegerField(default=-1)
    s16_e1 = models.IntegerField()
    s16_e2 = models.IntegerField()
    s16_e3 = models.IntegerField()
    s16_e4 = models.IntegerField()
    s16_e5 = models.FloatField()
    s16_e6 = models.IntegerField()
    s16_1e3 = models.IntegerField(default=-1)
    s16_e7 = models.IntegerField(default=-1)

    s17_e1_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e1comment', default=1)
    s17_e2_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e2comment', default=1)
    s17_e3_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e3comment', default=1)
    s17_e4_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e4comment', default=1)
    s17_e5_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e5comment', default=1)
    s17_e6_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e6comment', default=1)
    s17_e7_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e7comment', default=1)
    s17_e8_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e8comment', default=1)
    s17_e9_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                       related_name='ven1s17e9comment', default=1)
    s17_e10_comment = models.ForeignKey(acc.models.Comment, on_delete=models.PROTECT,
                                        related_name='ven1s17e10comment', default=1)

    def __str__(self):
        return 'Ventilator : ' + str(self.Licence)
