from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, DeviceViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
