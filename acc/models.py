from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels



class ad_az_Status(models.Model):
    status = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = "Status"
    def __str__(self):
        return  str(self.status)
class ad_req_Status(models.Model):
    status = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = "req_Status"

    def __str__(self):
        return str(self.status)
class ad_acc_Status(models.Model):
    status = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = "accStatus"
    def __str__(self):
        return str(self.status)


class ad_test_type(models.Model):#class
    type = models.CharField(max_length=30)
    def __str__(self):
        return str(self.type)
class ad_test_type2(models.Model):#bf/cf ac/dc
    type = models.CharField(max_length=30)
    def __str__(self):
        return str(self.type)


class Country(models.Model):
    name = models.TextField()
    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return self.name
class State(models.Model):
    name = models.TextField()
    country = models.ForeignKey(Country , on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class City(models.Model):
    state_name = models.ForeignKey(State ,on_delete=models.CASCADE)
    name = models.TextField()
    class Meta:
        verbose_name_plural = "Cities"
    def __str__(self):
        return self.name



class Section(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class Parameters(models.Model):
    name = models.TextField()
    value = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class aUserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')
    signature = models.ImageField(upload_to='signature/',null=True,blank=True)
    status = models.ForeignKey(ad_acc_Status,on_delete=models.PROTECT)
    def __str__(self):
        return self.user.first_name
    


class Hospital(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City , on_delete=models.CASCADE)
    address = models.TextField()
    p_name = models.TextField()
    p_phone = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name) + ' ' + str(self.city.name)



class Company(models.Model):
    name = models.TextField()
    en_name = models.TextField()
    country = models.ForeignKey(Country , on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Companies"
    def __str__(self):
        return self.name


class device_type(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name




class Device(models.Model):
    name = models.TextField()
    type = models.ForeignKey(device_type , on_delete=models.CASCADE)
    creator = models.ForeignKey(Company , on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Cal_device(models.Model):
    name = models.TextField()
    type = models.ForeignKey(device_type , on_delete=models.CASCADE)
    creator = models.ForeignKey(Company , on_delete=models.CASCADE)
    serial = models.CharField(max_length=30)
    calibration_date = models.DateField()
    calibration_Expire_date = models.DateField()
    def __str__(self):
        return self.name


class All_Device(models.Model):
    name = models.ForeignKey(Device , on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE)
    section = models.ForeignKey(Section , on_delete=models.CASCADE)
    serial_number = models.TextField(null=True,blank=True)
    property_number = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.name) + ' - ' + str(self.hospital.name) + ' - ' + str(self.serial_number)


class Request(models.Model):
    date = jmodels.jDateField()
    hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.ForeignKey(ad_req_Status,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.number)



class record(models.Model):
    number= models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)
class licence(models.Model):
    number = models.IntegerField()
    def __str__(self):
        return  str(self.number)


class accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(device_type,on_delete=models.PROTECT)
    company = models.ForeignKey(Company,on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = "Accessories"
    def __str__(self):
        return str(self.name)


class ad_excel_arg(models.Model):
    arg = models.TextField()
    order = models.IntegerField()
    def __str__(self):
        return self.arg





class comment_cant_test(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_monitor_spo2(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_monitor_spo2(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)




class qualitive_comment_monitor_ecg(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_monitor_ecg(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)




class qualitive_comment_monitor_nibp(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_monitor_nibp(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)




class qualitive_comment_monitor_safety(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_monitor_safety(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_aed(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_aed(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)




class qualitive_comment_anesthesia_machine(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_anesthesia_machine(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_defibrilator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_defibrilator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_ecg(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_ecg(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)


class qualitive_comment_electrocouter(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_electrocouter(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_monometer(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_monometer(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_syringe_pump(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_syringe_pump(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)


class qualitive_comment_spo2(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_spo2(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)



class qualitive_comment_infusion_pump(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_infusion_pump(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)




class qualitive_comment_suction(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_suction(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)





class qualitive_comment_ventilator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_ventilator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)





class qualitive_comment_flowmeter(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_flowmeter(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)





class qualitive_comment_ancobator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)
class quantitive_comment_ancobator(models.Model):
    comment = models.CharField(max_length=50)
    def __str__(self):
       return  str(self.comment)