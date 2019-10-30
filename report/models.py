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

class report(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(record, on_delete=models.CASCADE, related_name='rr')
    licence = models.ForeignKey(licence, on_delete=models.CASCADE, related_name='me1licence')
    status = models.ForeignKey(acc.models.ad_az_Status, on_delete=models.PROTECT)
    
    monitor_spo2_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_spo2, related_name='rmspo2totalcomment')
    monitor_ecg_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_ecg, related_name='rmetotalcomment')
    monitor_nibp_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_nibp, related_name='rmntotalcomment')
    monitor_safety_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monitor_safety, related_name='rmsafetotalcomment')
    defibrilator_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_defibrilator, related_name='rdetotalcomment')
    aed_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_aed, related_name='raedtotalcomment')
    ecg_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_ecg, related_name='recgtotalcomment')
    infusion_pump_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_infusion_pump, related_name='riptotalcomment')
    syringe_pump_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_syringe_pump, related_name='rsptotalcomment')
    spo2_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_spo2, related_name='rspo2totalcomment')
    flowmeter_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_flowmeter, related_name='rfmtotalcomment')
    anesthesia_machine_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_anesthesia_machine, related_name='ramtotalcomment')
    ventilator_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_ventilator, related_name='rvetotalcomment')
    suction_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_suction, related_name='rsutotalcomment')
    electrocauter_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_electrocouter, related_name='rectotalcomment')
    monometer_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_monometer, related_name='rmmtotalcomment')
    cant_test_totalcomment = models.ManyToManyField(acc.models.qualitive_comment_cant_test, related_name='rcttotalcomment')
    
    is_done = models.BooleanField(default=False)

