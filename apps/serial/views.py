from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .models import Task
from .pagination import TaskPagination
from .permissions import IsAuthenticatedOrReadOnly
from .serializers import TaskSerializer


class TaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'id']
    ordering = ['id']

