from django.apps import AppConfig


class AbandonedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.abandoned'
    verbose_name = 'Каталог заброшенных мест'