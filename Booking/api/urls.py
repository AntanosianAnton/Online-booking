from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MasterViewSet, ServiceViewSet, AppointmentViewSet

router = SimpleRouter()
router.register('masters', MasterViewSet)
router.register('services', ServiceViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
