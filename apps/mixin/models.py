from django.db import models

class Mixin(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    created = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Human(Mixin):
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    addres = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст статьи')
    category = models.CharField(max_length=100, verbose_name='Категория')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=120, verbose_name='ФИО или название компании')
    notes = models.TextField(blank=True, verbose_name='Заметки')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, verbose_name='Электронная почта')
    address = models.CharField(max_length=300, blank=True, verbose_name='Адрес')
    is_active = models.BooleanField(default=True, verbose_name='Клиент активен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name

# DRY = Dont repeat yorself