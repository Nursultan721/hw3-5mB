from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название магазина')
    description = models.TextField(blank=True, verbose_name='Описание магазина')
    address = models.CharField(max_length=300, verbose_name='Адрес магазина')
    phone = models.CharField(
        max_length=30,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^[0-9+()\-\s]+$',
                message='Телефон может содержать только цифры, пробелы и символы +, (, ), -.',
            )
        ],
        verbose_name='Контактный телефон',
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=Decimal('5.00'),
        validators=[
            MinValueValidator(Decimal('0.00')),
            MaxValueValidator(Decimal('5.00')),
        ],
        verbose_name='Рейтинг магазина',
    )
    is_active = models.BooleanField(default=True, verbose_name='Магазин активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title