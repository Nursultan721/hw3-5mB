from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Product
from .pagination import ProductPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer


class ProductApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'in_have', 'discount']
    search_fields = ['title', 'description', 'category']
    ordering_fields = ['title', 'price', 'discount']
    ordering = ['title']


class PoductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
