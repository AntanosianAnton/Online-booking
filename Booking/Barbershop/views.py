from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils import timezone

from .models import Barber, Service, Appointment


class HomePageView(TemplateView):
    template_name = 'barbershop/home.html'

    def appointment_list(request):
        appointments = Appointment.objects.filter(
            date__gte=timezone.now() - timezone.timedelta(days=56)
        ).order_by('-date', 'time')
        paginator = Paginator(appointments, 28)
        page = request.GET.get('page')
        appointments_page = paginator.get_page(page)
        return render(
            request,
            'home.html', {'appointments_page': appointments_page}
        )


class BarberPageView(TemplateView):
    template_name = 'barbers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barbers'] = Barber.objects.all()
        return context


class ServicePageView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class AppointmentPageView(TemplateView):
    template_name = 'appointment.html'

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
