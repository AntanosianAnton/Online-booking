from django.contrib import admin
from .models import Appointment, Master, Service


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'barber',
        'customer_name',
        'customer_phone_number',
        'service',
        'date',
        'time'
        )
    


admin.site.register(Appointment)
admin.site.register(Master)
admin.site.register(Service)
