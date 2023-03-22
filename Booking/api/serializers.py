from rest_framework import serializers
from Barbershop.models import Master, Service, Appointment

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    barber = MasterSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)
        return appointment
