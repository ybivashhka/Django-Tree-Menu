"""
Views для демо-страниц
"""
from django.shortcuts import render


def home(request):
    """Главная страница"""
    return render(request, 'demo/base.html', {
        'page_title': 'Главная страница',
        'current_page': 'home'
    })


def about(request):
    """Страница О нас"""
    return render(request, 'demo/base.html', {
        'page_title': 'О нас',
        'current_page': 'about'
    })


def services(request):
    """Страница Услуги"""
    return render(request, 'demo/base.html', {
        'page_title': 'Услуги',
        'current_page': 'services'
    })


def products(request):
    """Страница Продукты"""
    return render(request, 'demo/base.html', {
        'page_title': 'Продукты',
        'current_page': 'products'
    })


def contact(request):
    """Страница Контакты"""
    return render(request, 'demo/base.html', {
        'page_title': 'Контакты',
        'current_page': 'contact'
    })


def blog(request):
    """Страница Блог"""
    return render(request, 'demo/base.html', {
        'page_title': 'Блог',
        'current_page': 'blog'
    })


def news(request):
    """Страница Новости"""
    return render(request, 'demo/base.html', {
        'page_title': 'Новости',
        'current_page': 'news'
    })


def faq(request):
    """Страница FAQ"""
    return render(request, 'demo/base.html', {
        'page_title': 'FAQ',
        'current_page': 'faq'
    })


# Подкатегории услуг
def web_development(request):
    """Страница Веб-разработка"""
    return render(request, 'demo/base.html', {
        'page_title': 'Веб-разработка',
        'current_page': 'web_development'
    })


def mobile_apps(request):
    """Страница Мобильные приложения"""
    return render(request, 'demo/base.html', {
        'page_title': 'Мобильные приложения',
        'current_page': 'mobile_apps'
    })


def design(request):
    """Страница Дизайн"""
    return render(request, 'demo/base.html', {
        'page_title': 'Дизайн',
        'current_page': 'design'
    })


def frontend(request):
    """Страница Frontend"""
    return render(request, 'demo/base.html', {
        'page_title': 'Frontend разработка',
        'current_page': 'frontend'
    })


def backend(request):
    """Страница Backend"""
    return render(request, 'demo/base.html', {
        'page_title': 'Backend разработка',
        'current_page': 'backend'
    })


# Подкатегории продуктов
def software(request):
    """Страница Программное обеспечение"""
    return render(request, 'demo/base.html', {
        'page_title': 'Программное обеспечение',
        'current_page': 'software'
    })


def hardware(request):
    """Страница Оборудование"""
    return render(request, 'demo/base.html', {
        'page_title': 'Оборудование',
        'current_page': 'hardware'
    })


def crm_systems(request):
    """Страница CRM системы"""
    return render(request, 'demo/base.html', {
        'page_title': 'CRM системы',
        'current_page': 'crm_systems'
    })


def erp_systems(request):
    """Страница ERP системы"""
    return render(request, 'demo/base.html', {
        'page_title': 'ERP системы',
        'current_page': 'erp_systems'
    })


# Подкатегории блога
def tech_blog(request):
    """Страница Технологии"""
    return render(request, 'demo/base.html', {
        'page_title': 'Технологии',
        'current_page': 'tech_blog'
    })


def news_blog(request):
    """Страница Новости"""
    return render(request, 'demo/base.html', {
        'page_title': 'Новости',
        'current_page': 'news_blog'
    }) 