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
    totalcomment = models.TextField(null=True, blank= True)
    is_done = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "سابقه گزارشات"
    def __str__(self):
        return  'report_summary' + str(self.licence)
