from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet

router = DefaultRouter()
# this means we have api/v1/teams will give ClientViewSet
router.register("teams", TeamViewSet, basename="teams")

urlpatterns = [
    path('', include(router.urls))
]