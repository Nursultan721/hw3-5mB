from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Visitors, Zone
from .pagination import CatalogPagination
from .serializers import VisitorsSerializer, ZoneSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    pagination_class = CatalogPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['visitors_count']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['title', 'visitors_count', 'created_at']
    ordering = ['-created_at']


class VisitorsViewSet(viewsets.ModelViewSet):
    queryset = Visitors.objects.select_related('zone').all()
    serializer_class = VisitorsSerializer
    pagination_class = CatalogPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['zone', 'is_allowed']
    search_fields = ['name', 'title', 'description', 'zone__title']
    ordering_fields = ['name', 'created_at', 'is_allowed']
    ordering = ['-created_at']