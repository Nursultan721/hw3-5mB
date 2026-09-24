from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VisitorsViewSet, ZoneViewSet


router = DefaultRouter()
router.register('zones', ZoneViewSet, basename='zone')
router.register('visitors', VisitorsViewSet, basename='visitor')

urlpatterns = [
    path('', include(router.urls)),
]