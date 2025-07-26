"""
URLs для демо-страниц
"""
from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Услуги и подкатегории
    path('services/', views.services, name='services'),
    path('services/web-development/', views.web_development, name='web_development'),
    path('services/mobile-apps/', views.mobile_apps, name='mobile_apps'),
    path('services/design/', views.design, name='design'),
    path('services/web-development/frontend/', views.frontend, name='frontend'),
    path('services/web-development/backend/', views.backend, name='backend'),
    
    # Продукты и подкатегории
    path('products/', views.products, name='products'),
    path('products/software/', views.software, name='software'),
    path('products/hardware/', views.hardware, name='hardware'),
    path('products/software/crm/', views.crm_systems, name='crm_systems'),
    path('products/software/erp/', views.erp_systems, name='erp_systems'),
    
    path('contact/', views.contact, name='contact'),
    
    # Блог и подкатегории
    path('blog/', views.blog, name='blog'),
    path('blog/tech/', views.tech_blog, name='tech_blog'),
    path('blog/news/', views.news_blog, name='news_blog'),
    
    path('faq/', views.faq, name='faq'),
] 