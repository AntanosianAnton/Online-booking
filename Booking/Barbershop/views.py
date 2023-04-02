from django.views.generic import TemplateView
from .models import Barber, Service, Appointment


class HomePageView(TemplateView):
    template_name = 'home.html'


class BarberPageView(TemplateView):
    template_name = 'Barbershop/templates/barbers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbers'] = Barber.objects.all()
        return context


class ServicePageView(TemplateView):
    template_name = 'Barbershop/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class AppointmentPageView(TemplateView):
    template_name = 'Barbershop/appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbers'] = Barber.objects.all()
        context['services'] = Service.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        barber = Barber.objects.get(id=request.POST.get('barber'))
        service = Service.objects.get(id=request.POST.get('service'))
        date = request.POST.get('date')
        time = request.POST.get('time')
        customer_name = request.POST.get('customer_name')
        customer_phone_number = request.POST.get('customer_phone_number')
        Appointment.objects.create(
            barber_name=barber,
            service=service,
            date=date,
            time=time,
            customer_name=customer_name,
            customer_phone_number=customer_phone_number
        )
        return self.render_to_response(self.get_context_data())
