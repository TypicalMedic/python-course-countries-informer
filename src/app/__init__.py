"""Модуль приложения"""

from app.celery import app as celery_app


__all__ = ("celery_app",)
