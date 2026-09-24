from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CatalogBase(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class Zone(CatalogBase):
    location = models.CharField(max_length=300, verbose_name='Локация')
    visitors_count = models.PositiveIntegerField(default=0, verbose_name='Количество посетителей')
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        verbose_name='Широта',
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        verbose_name='Долгота',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заброшенная зона'
        verbose_name_plural = 'Заброшенные зоны'

    def __str__(self):
        return self.title


class Visitors(CatalogBase):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='visitors',
        verbose_name='Зона',
    )
    name = models.CharField(max_length=150, verbose_name='Имя посетителя')
    is_allowed = models.BooleanField(default=False, verbose_name='Вход разрешен')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'

    def __str__(self):
        return self.name