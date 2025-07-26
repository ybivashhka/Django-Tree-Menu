"""
Команда для создания демо-данных меню

Перед запуском этой команды убедитесь, что:
1. Миграции созданы: python manage.py makemigrations tree_menu
2. Миграции применены: python manage.py migrate

Эта команда создает:
- Главное меню (main_menu) с пунктами: Главная, О нас, Услуги, Продукты, Контакты
- Подкатегории для услуг (Веб-разработка, Мобильные приложения, Дизайн)
- Подкатегории для продуктов (Программное обеспечение, Оборудование)
- Дополнительное меню (secondary_menu) с блогом и FAQ

Использование:
    python manage.py create_demo_menu
"""
from django.core.management.base import BaseCommand
from apps.tree_menu.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Создает демо-данные для древовидного меню'

    def handle(self, *args, **options):
        self.stdout.write('Создание демо-данных для меню...')
        
        # Проверяем, что таблицы существуют
        try:
            Menu.objects.first()
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    'Ошибка: Таблицы базы данных не созданы. '
                    'Выполните сначала:\n'
                    'python manage.py makemigrations tree_menu\n'
                    'python manage.py migrate'
                )
            )
            return
        
        # Создаем главное меню
        main_menu, created = Menu.objects.get_or_create(
            name='main_menu',
            defaults={'description': 'Главное меню сайта'}
        )
        
        if created:
            self.stdout.write(f'Создано меню: {main_menu.name}')
        
        # Создаем пункты главного меню
        home_item, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Главная',
            defaults={
                'url': '/',
                'order': 1
            }
        )
        
        about_item, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='О нас',
            defaults={
                'url': '/about/',
                'order': 2
            }
        )
        
        # Создаем "Услуги" с подкатегориями
        services_item, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Услуги',
            defaults={
                'url': '/services/',
                'order': 3
            }
        )
        
        # Подкатегории услуг
        web_dev, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Веб-разработка',
            parent=services_item,
            defaults={
                'url': '/services/web-development/',
                'order': 1
            }
        )
        
        mobile_dev, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Мобильные приложения',
            parent=services_item,
            defaults={
                'url': '/services/mobile-apps/',
                'order': 2
            }
        )
        
        design, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Дизайн',
            parent=services_item,
            defaults={
                'url': '/services/design/',
                'order': 3
            }
        )
        
        # Подкатегории веб-разработки
        MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Frontend',
            parent=web_dev,
            defaults={
                'url': '/services/web-development/frontend/',
                'order': 1
            }
        )
        
        MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Backend',
            parent=web_dev,
            defaults={
                'url': '/services/web-development/backend/',
                'order': 2
            }
        )
        
        # Создаем "Продукты" с подкатегориями
        products_item, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Продукты',
            defaults={
                'url': '/products/',
                'order': 4
            }
        )
        
        # Подкатегории продуктов
        software, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Программное обеспечение',
            parent=products_item,
            defaults={
                'url': '/products/software/',
                'order': 1
            }
        )
        
        hardware, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Оборудование',
            parent=products_item,
            defaults={
                'url': '/products/hardware/',
                'order': 2
            }
        )
        
        # Подкатегории ПО
        MenuItem.objects.get_or_create(
            menu=main_menu,
            title='CRM системы',
            parent=software,
            defaults={
                'url': '/products/software/crm/',
                'order': 1
            }
        )
        
        MenuItem.objects.get_or_create(
            menu=main_menu,
            title='ERP системы',
            parent=software,
            defaults={
                'url': '/products/software/erp/',
                'order': 2
            }
        )
        
        contact_item, _ = MenuItem.objects.get_or_create(
            menu=main_menu,
            title='Контакты',
            defaults={
                'url': '/contact/',
                'order': 5
            }
        )
        
        # Создаем дополнительное меню
        secondary_menu, created = Menu.objects.get_or_create(
            name='secondary_menu',
            defaults={'description': 'Дополнительное меню'}
        )
        
        if created:
            self.stdout.write(f'Создано меню: {secondary_menu.name}')
        
        # Создаем пункты дополнительного меню
        blog_item, _ = MenuItem.objects.get_or_create(
            menu=secondary_menu,
            title='Блог',
            defaults={
                'url': '/blog/',
                'order': 1
            }
        )
        
        # Подкатегории блога
        MenuItem.objects.get_or_create(
            menu=secondary_menu,
            title='Технологии',
            parent=blog_item,
            defaults={
                'url': '/blog/tech/',
                'order': 1
            }
        )
        
        MenuItem.objects.get_or_create(
            menu=secondary_menu,
            title='Новости',
            parent=blog_item,
            defaults={
                'url': '/blog/news/',
                'order': 2
            }
        )
        
        faq_item, _ = MenuItem.objects.get_or_create(
            menu=secondary_menu,
            title='FAQ',
            defaults={
                'url': '/faq/',
                'order': 2
            }
        )
        
        self.stdout.write(
            self.style.SUCCESS('Демо-данные успешно созданы!')
        )
        self.stdout.write('Доступ к админке: http://127.0.0.1:8000/admin/')
        self.stdout.write('Логин: admin, пароль: admin') 