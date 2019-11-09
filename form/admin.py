from django.contrib import admin

from .models import *

class formAdmin(admin.ModelAdmin):
    list_display = ("__str__","licence", "is_recal", "is_done", "status", "date","request","device", "user", )
admin.site.register(monitor_spo2_1,formAdmin)
admin.site.register(monitor_ecg_1,formAdmin)
admin.site.register(monitor_nibp_1,formAdmin)
admin.site.register(monitor_safety_1,formAdmin)
admin.site.register(aed_1,formAdmin)
admin.site.register(anesthesia_machine_1,formAdmin)
admin.site.register(defibrilator_1,formAdmin)
admin.site.register(ecg_1,formAdmin)
admin.site.register(electrocauter_1,formAdmin)
admin.site.register(spo2_1,formAdmin)
admin.site.register(syringe_pump_1,formAdmin)
admin.site.register(suction_1,formAdmin)