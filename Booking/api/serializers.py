from rest_framework import serializers
from Barbershop.models import Barber, Service, Appointment


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    service = serializers.SlugRelatedField(
        slug_field='service_name',
        queryset=Service.objects.all())
    barber = serializers.SlugRelatedField(
        slug_field='barber_name',
        queryset=Barber.objects.all())

    class Meta:
        model = Appointment
        fields = ['id',
                  'customer_name',
                  'customer_phone_number',
                  'date', 'time', 'service', 'barber']

    def create(self, validated_data):
        existing_appointments = Appointment.objects.filter(
            barber=validated_data['barber'],
            date=validated_data['date'],
            time=validated_data['time']
            )
        if existing_appointments:
            raise serializers.ValidationError(
                'Выберите другое время или дату для записи'
                )
        appointment = Appointment.objects.create(**validated_data)
        return appointment
