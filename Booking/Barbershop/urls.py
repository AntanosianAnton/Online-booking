from django.urls import path
from .views import (HomePageView,
                    BarberPageView,
                    ServicePageView,
                    AppointmentPageView)

app_name = 'Barbershop'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('barbers/', BarberPageView.as_view(), name='barbers'),
    path('services/', ServicePageView.as_view(), name='services'),
    path('appointment/', AppointmentPageView.as_view(), name='appointment'),
]
