from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class AdAzStatus(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "وضعیت های آزمایش"

    def __str__(self):
        return str(self.status)


class AdReqStatus(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "وضعیت های درخواست"

    def __str__(self):
        return str(self.status)


class AdAccStatus(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "سلسله مراتب حسابها"

    def __str__(self):
        return str(self.status)


class AdTestType0(models.Model):  # class
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "نوع آزمایش"

    def __str__(self):
        return str(self.type)


class AdTestType(models.Model):  # class
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "کلاس تست"

    def __str__(self):
        return str(self.type)


class AdTestType1(models.Model):  # bf/cf ac/dc
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "کلاس تست 2"

    def __str__(self):
        return str(self.type)


class Country(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name_plural = "کشور ها"

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    eng_name = models.TextField()

    class Meta:
        verbose_name_plural = "استان ها"

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.TextField()
    eng_name = models.TextField()

    class Meta:
        verbose_name_plural = "شهر ها"

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.TextField()
    eng_name = models.TextField()

    class Meta:
        verbose_name_plural = "بخش های بیمارستان"

    def __str__(self):
        return self.name


class Parameters(models.Model):
    name = models.TextField()
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "پارامتر ها"

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatar/')
    signature = models.ImageField(
        upload_to='signature/', null=True, blank=True)
    status = models.ForeignKey(AdAccStatus, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "1_مشخصات کاربران"

    def __str__(self):
        return self.user.first_name


class Hospital(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "2_بیمارستان ها"

    def __str__(self):
        return str(self.name) + ' ' + str(self.city.name)


class Company(models.Model):
    name = models.TextField()
    en_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "شرکت های سازنده"

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name_plural = "نوع دستگاه ها"

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.TextField()
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    creator = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "لیست دستگاه"

    def __str__(self):
        return self.name


class CalDevice(models.Model):
    name = models.TextField()
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    creator = models.ForeignKey(Company, on_delete=models.CASCADE)
    serial = models.CharField(max_length=30)
    calibration_date = models.DateField()
    calibration_Expire_date = models.DateField()

    class Meta:
        verbose_name_plural = "4_دستگاه های کنترل کیفی"

    def __str__(self):
        return self.name


class AllDevice(models.Model):
    name = models.ForeignKey(Device, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    serial_number = models.TextField(null=True, blank=True)
    property_number = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "3_دستگاه های ثبت شده"

    def __str__(self):
        return str(self.name) + ' - ' + str(self.hospital.name) + ' - ' + str(self.serial_number)


class Request(models.Model):
    date = jmodels.jDateField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    number = models.IntegerField()
    status = models.ForeignKey(
        AdReqStatus, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "5_لیست درخواست ها"

    def __str__(self):
        return str(self.number)


class Record(models.Model):
    number = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name_plural = "شماره رکورد"

    def __str__(self):
        return str(self.number)


class Licence(models.Model):
    number = models.IntegerField()

    class Meta:
        verbose_name_plural = "شماره گواهی"

    def __str__(self):
        return str(self.number)


class Accessory(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(DeviceType, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "لوازم جانبی"

    def __str__(self):
        return str(self.name)


class AdExcelArg(models.Model):
    arg = models.TextField()

    class Meta:
        verbose_name_plural = "آرگومان اکسل"

    def __str__(self):
        return self.arg


class Comment(models.Model):
    comment = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "توضیحات"

    def __str__(self):
        return str(self.comment)
