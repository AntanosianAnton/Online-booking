from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import BarberViewSet, ServiceViewSet, AppointmentViewSet

router = SimpleRouter()
router.register('masters', BarberViewSet)
router.register('services', ServiceViewSet)
router.register('records', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
