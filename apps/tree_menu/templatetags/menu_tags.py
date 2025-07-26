"""
Template tags для древовидного меню
"""
from django import template
from django.template.loader import render_to_string
from ..services import MenuService

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Отрисовать древовидное меню"""
    request = context.get('request')
    current_path = request.path if request else None
    
    # Получаем данные меню
    tree_data = MenuService.get_menu_data(menu_name, current_path)
    
    return {
        'tree_data': tree_data,
        'menu_name': menu_name
    } 