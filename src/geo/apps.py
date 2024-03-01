"""
Конфигурация приложений базы данных
"""
from django.apps import AppConfig


class GeoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "geo"
    verbose_name = "Города и страны"
