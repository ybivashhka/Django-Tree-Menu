"""
URL configuration for django-tree-menu project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.demo.urls')),
] 