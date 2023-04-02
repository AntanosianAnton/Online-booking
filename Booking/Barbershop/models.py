from django.db import models
from datetime import timedelta
from typing import List, Tuple
import datetime
import calendar
from django.contrib.auth import get_user_model


User = get_user_model()


class Barber(models.Model):
    """Модель мастера"""
    barber_name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.barber_name


class Service(models.Model):
    """Модель услуги"""
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(default=timedelta(minutes=0))

    def __str__(self):
        return str(self.service_name) + ": $" + str(self.price)


class Appointment(models.Model):
    """Модель записи"""
    barber_name = models.ForeignKey(Barber, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    # забиндить только определенные часы, c 9:00 до 21:00
    time = models.CharField(max_length=5, choices=(
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00')
    ))

    def __str__(self):
        return (f"{self.customer_name} - Вы записаны на "
                f"{self.service.service_name} дата: {self.date} {self.time}")
