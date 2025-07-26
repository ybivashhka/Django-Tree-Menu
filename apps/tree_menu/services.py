"""
Сервисы для работы с древовидным меню
"""
from django.core.cache import cache
from django.urls import resolve
from .models import Menu, MenuItem


class MenuService:
    """Сервис для работы с меню"""
    
    @staticmethod
    def get_menu_data(menu_name, current_path=None):
        """Получить данные меню с кэшированием"""
        cache_key = f'menu_{menu_name}_{current_path}'
        cached_data = cache.get(cache_key)
        
        if cached_data is not None:
            return cached_data
        
        try:
            menu = Menu.objects.prefetch_related(
                'items__children__children'
            ).get(name=menu_name, is_active=True)
        except Menu.DoesNotExist:
            return None
        
        # Определяем активный пункт
        active_item = None
        if current_path:
            active_item = MenuService._find_active_item(menu, current_path)
        
        # Строим дерево
        tree = MenuService._build_tree(menu, active_item)
        
        # Кэшируем результат
        cache.set(cache_key, tree, 300)  # 5 минут
        
        return tree
    
    @staticmethod
    def _find_active_item(menu, current_path):
        """Найти активный пункт меню"""
        for item in menu.items.all():
            if item.get_url() == current_path:
                return item
        return None
    
    @staticmethod
    def _build_tree(menu, active_item):
        """Построить дерево меню"""
        def build_branch(items, level=0):
            branch = []
            for item in items:
                if not item.is_active:
                    continue
                
                # Определяем, нужно ли развернуть этот пункт
                should_expand = False
                if active_item:
                    # Развернуть если это активный пункт или его предок
                    if item == active_item or item in active_item.get_ancestors():
                        should_expand = True
                    # Развернуть первый уровень потомков активного пункта
                    elif (active_item.parent == item or 
                          (active_item.parent and active_item.parent.parent == item)):
                        should_expand = True
                
                node = {
                    'item': item,
                    'children': build_branch(item.children.all(), level + 1) if should_expand else [],
                    'is_active': item == active_item,
                    'is_expanded': should_expand,
                    'level': level
                }
                branch.append(node)
            return branch
        
        return {
            'menu': menu,
            'items': build_branch(menu.items.filter(parent=None))
        }


class MenuRenderer:
    """Рендерер для отображения меню"""
    
    @staticmethod
    def render_menu_html(tree_data):
        """Рендерить HTML меню"""
        if not tree_data:
            return ""
        
        html = ['<ul class="tree-menu">']
        html.extend(MenuRenderer._render_items(tree_data['items']))
        html.append('</ul>')
        
        return '\n'.join(html)
    
    @staticmethod
    def _render_items(items):
        """Рендерить пункты меню"""
        html = []
        for node in items:
            item = node['item']
            children = node['children']
            is_active = node['is_active']
            is_expanded = node['is_expanded']
            
            # CSS классы
            classes = ['menu-item']
            if is_active:
                classes.append('active')
            if children:
                classes.append('has-children')
            if is_expanded:
                classes.append('expanded')
            
            html.append(f'<li class="{" ".join(classes)}">')
            
            # Ссылка
            url = item.get_url()
            html.append(f'<a href="{url}" class="menu-link">')
            html.append(f'<span class="menu-title">{item.title}</span>')
            if children:
                html.append('<i class="menu-toggle fas fa-chevron-down"></i>')
            html.append('</a>')
            
            # Подменю
            if children:
                html.append('<ul class="submenu">')
                html.extend(MenuRenderer._render_items(children))
                html.append('</ul>')
            
            html.append('</li>')
        
        return html 