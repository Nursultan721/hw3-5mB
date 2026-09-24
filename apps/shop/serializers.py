from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'id',
            'title',
            'description',
            'address',
            'phone',
            'rating',
            'is_active',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError('Название магазина не может быть пустым.')
        return value

    def validate_address(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError('Адрес магазина не может быть пустым.')
        return value