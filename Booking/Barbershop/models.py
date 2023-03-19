from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User


class Master(models.Model):
    """Модель мастера"""
    master = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # other fields...

    def __str__(self):
        return self.name


class Service(models.Model):
    """Модель услуги"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(default=timedelta(hours=1))
    # other fields...

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """Модель записи"""
    barber = models.ForeignKey(Master, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    # other fields...

    def __str__(self):
        return (f"{self.customer_name} - Вы записаны на {self.service.name} дата: {self.date} {self.time}")