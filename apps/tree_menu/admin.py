"""
Админка для древовидного меню
"""
from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    """Inline для пунктов меню"""
    model = MenuItem
    extra = 1
    fields = ['title', 'url', 'named_url', 'order', 'is_active']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Админка для меню"""
    list_display = ['name', 'description', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Админка для пунктов меню"""
    list_display = ['title', 'menu', 'parent', 'url_display', 'order', 'is_active']
    list_filter = ['menu', 'is_active', 'parent']
    search_fields = ['title', 'url', 'named_url']
    list_editable = ['order', 'is_active']
    ordering = ['menu', 'order']

    def url_display(self, obj):
        """Отображение URL"""
        if obj.url:
            return obj.url
        elif obj.named_url:
            return f"named: {obj.named_url}"
        return "-"
    url_display.short_description = 'URL' 