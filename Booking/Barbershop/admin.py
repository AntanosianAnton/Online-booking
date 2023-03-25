from django.contrib import admin
from .models import Appointment, Barber, Service


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
    list_filter = (
        'customer_name',
        'customer_phone_number',
        'service',
        'date',
        'barber',
    )
    search_fields = (
        'customer_name',
        'customer_phone_number',
        'service',
        'date',
        'barber',
    )



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'duration'
    )


admin.site.register(Barber)
# admin.site.register(Appointment)
# admin.site.register(Service)
