from django.contrib import admin
from .models import Device,Company

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'model')

admin.site.register(Device ,DeviceAdmin)
admin.site.register(Company)
