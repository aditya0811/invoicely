from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet

router = DefaultRouter()
# this means we have api/v1/invoice will give ClientViewSet
router.register("invoices", InvoiceViewSet, basename="invoices")

urlpatterns = [
    path('', include(router.urls))
]