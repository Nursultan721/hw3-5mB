from django.urls import path

from .views import (
    ClientDetailView,
    ClientListCreateView,
    PostDetailView,
    PostListCreateView,
)


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
]

