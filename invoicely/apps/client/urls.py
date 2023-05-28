from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()
# this means we have api/v1/clients will give ClientViewSet
router.register("clients", ClientViewSet, basename="clients")

urlpatterns = [
    path('', include(router.urls))
]