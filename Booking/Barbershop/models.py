from django.db import models
from datetime import timedelta
from django.contrib.auth import get_user_model


User = get_user_model()


class Barber(models.Model):
    """Модель мастера"""
    # master = models.OneToOneField(User, on_delete=models.CASCADE)
    # убрал это поле, без него работает
    barber_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # other fields...

    def __str__(self):
        return self.barber_name


class Service(models.Model):
    """Модель услуги"""
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(default=timedelta(minutes=0))
    # other fields...

    def __str__(self):
        return str(self.service_name) + ": $" + str(self.price)


class Appointment(models.Model):
    """Модель записи"""
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    # забиндить только определенные часы, c 9:00 до 21:00
    time = models.TimeField()
    # other fields...

    def __str__(self):
        return (f"{self.customer_name} - Вы записаны на"
                f"{self.service.service_name} дата: {self.date} {self.time}")
