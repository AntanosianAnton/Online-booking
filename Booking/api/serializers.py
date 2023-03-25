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
    service = serializers.SlugRelatedField(slug_field='service_name', queryset=Service.objects.all())
    barber = serializers.SlugRelatedField(slug_field='barber_name', queryset=Barber.objects.all())

    class Meta:
        model = Appointment
        fields = ['id', 'date', 'time', 'service', 'barber']

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)
        return appointment

