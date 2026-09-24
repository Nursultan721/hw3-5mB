from rest_framework import serializers

from .models import Visitors, Zone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = [
            'id',
            'title',
            'description',
            'location',
            'visitors_count',
            'latitude',
            'longitude',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError('Название зоны не может быть пустым.')
        return value

    def validate_location(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError('Локация не может быть пустой.')
        return value


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = [
            'id',
            'zone',
            'title',
            'description',
            'name',
            'is_allowed',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError('Имя посетителя не может быть пустым.')
        return value