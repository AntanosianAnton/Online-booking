# Generated by Django 4.1.7 on 2023-03-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barbershop', '0002_auto_20230325_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(choices=[('09:00', '9 a.m.'), ('10:00', '10 a.m.'), ('11:00', '11 a.m.'), ('12:00', '12 p.m.'), ('13:00', '1 p.m.'), ('14:00', '2 p.m.'), ('15:00', '3 p.m.'), ('16:00', '4 p.m.'), ('17:00', '5 p.m.')]),
        ),
    ]
