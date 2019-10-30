from django.db import models

# Create your models here.
class report(models.Model):
    tt = models.ForeignKey(acc.models.ad_test_type0, on_delete=models.PROTECT)
    device = models.ForeignKey(acc.models.All_Device, on_delete=models.PROTECT)
    request = models.ForeignKey(acc.models.Request, on_delete=models.PROTECT)
    date = jmodels.jDateTimeField()
    user = models.ForeignKey(User, on_delete=models.PROTECT) 
    record = models.ForeignKey(acc.models.record, on_delete=models.CASCADE, related_name='ctr')
    totalcomment = models.ManyToManyField(acc.models.comment_cant_test, related_name='cttotalcomment')
    is_done = models.BooleanField(default=False)