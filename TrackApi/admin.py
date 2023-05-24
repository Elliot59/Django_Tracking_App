from django.contrib import admin
from .models import *


class DeviceUsageAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_name', 'hand_over_date')

    def employee_name(self, obj):
        return obj.device_log.employee.name


    def hand_over_date(self, obj):
        return obj.device_log.hand_over_date

class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'hand_over_date')

    def employee_name(self, obj):
        return obj.employee.name

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(DeviceCompany)
admin.site.register(DeviceUsage, DeviceUsageAdmin)
admin.site.register(DeviceLog, DeviceLogAdmin)

# Placeholder
admin.site.register(Subscription)
admin.site.register(Payment)