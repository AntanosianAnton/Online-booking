# Generated by Django 4.1.7 on 2023-03-26 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barbershop', '0005_alter_appointment_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='master',
        ),
    ]
