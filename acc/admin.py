from django.contrib import admin

from .models import *

class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "city")
admin.site.register(Hospital,HospitalAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state_name")
admin.site.register(City,CityAdmin)
admin.site.register(device_type)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
admin.site.register(Device,DeviceAdmin)
admin.site.register(Country)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
admin.site.register(Company,CompanyAdmin)
admin.site.register(Section)
admin.site.register(Cal_device,DeviceAdmin)

class All_DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital","section")
admin.site.register(All_Device,All_DeviceAdmin)

admin.site.register(Request)
admin.site.register(licence)

class excel_argAdmin(admin.ModelAdmin):
    list_display = ("arg", "order")

admin.site.register(ad_excel_arg, excel_argAdmin)


admin.site.register(accessory)
admin.site.register(aUserProfile)
admin.site.register(record)


# admin.site.register(qualitive_comment_monitor_nibp)
# admin.site.register(quantitive_comment_monitor_nibp)
admin.site.register(qualitive_comment_monitor_spo2)
admin.site.register(quantitive_comment_monitor_spo2)
# admin.site.register(qualitive_comment_monitor_ecg)
# admin.site.register(quantitive_comment_monitor_ecg)
# admin.site.register(qualitive_comment_monitor_safety)
# admin.site.register(quantitive_comment_monitor_safety)
# admin.site.register(qualitive_comment_aed)
# admin.site.register(quantitive_comment_aed)
# admin.site.register(qualitive_comment_anesthesia_machine)
# admin.site.register(quantitive_comment_anesthesia_machine)
admin.site.register(ad_test_type)
admin.site.register(ad_test_type2)
class status(admin.ModelAdmin):
    list_display = ("id", "status")
admin.site.register(ad_req_Status,status)
admin.site.register(ad_az_Status,status)

admin.site.register(ad_acc_Status)





