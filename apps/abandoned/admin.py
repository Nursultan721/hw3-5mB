from django.contrib import admin

from .models import Visitors, Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'visitors_count', 'latitude', 'longitude', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'location')


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zone', 'is_allowed', 'created_at')
    list_filter = ('is_allowed', 'zone', 'created_at')
    search_fields = ('name', 'title', 'description', 'zone__title')