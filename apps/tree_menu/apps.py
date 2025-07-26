"""
Конфигурация приложения tree_menu
"""
from django.apps import AppConfig


class TreeMenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.tree_menu'
    verbose_name = 'Древовидное меню' 