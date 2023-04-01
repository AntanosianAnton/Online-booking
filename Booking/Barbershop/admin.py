from django.contrib import admin
from .models import Appointment, Barber, Service


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'barber_name',
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
        'barber_name',
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
        'service_name',
        'price',
        'duration'
    )


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = (
        'barber_name',
    )
