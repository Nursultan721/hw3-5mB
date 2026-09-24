from django.contrib import admin

from .models import Client, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'category', 'views_count', 'is_published', 'created_at')
	list_filter = ('category', 'is_published', 'created_at')
	search_fields = ('title', 'description', 'category')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'phone', 'email', 'is_active', 'created_at')
	list_filter = ('is_active', 'created_at')
	search_fields = ('name', 'phone', 'email', 'address', 'notes')
