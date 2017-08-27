from django.contrib import admin
from .models import Type, Device

# Register your models here.
# admin.site.register(Type)
# admin.site.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('category', 'device_name', 'device_count')
    list_filter = ['category']
admin.site.register(Device, DeviceAdmin)