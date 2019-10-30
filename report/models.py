from django.db import models
import acc.models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels

# Create your models here.
class record(models.Model):
    number= models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)
class licence(models.Model):
    number = models.IntegerField()
    def __str__(self):
        return  str(self.number)
class comment(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return  str(self.number)


class report_monitor_spo2(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_monitor_ecg(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_monitor_nibp(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_monitor_safety(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_aed(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_defibrilator(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_ecg(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_infusion_pump(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_syringe_pump(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_spo2(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_flowmeter(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_anesthesia_machine(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_ventilator(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_suction(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_electrocauter(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_monometer(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

class report_cant_test(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    totalcomment = models.ManyToManyField(comment, related_name='rtotalcomment')
    is_done = models.BooleanField(default=False)

