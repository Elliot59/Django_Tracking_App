from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'device-company', DeviceCompanyViewSet)
router.register(r'device-usage', DeviceUsageViewSet)
router.register(r'device-logs', DeviceLogViewSet)
router.register(r'subscription', SubscriptionViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]