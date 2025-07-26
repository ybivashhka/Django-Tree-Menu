# 🌳 Django Tree Menu

Древовидное меню для Django с автоматическим разворачиванием активных пунктов.



## ✨ Особенности

- **Автоматическое разворачивание**: Активный пункт и все пункты выше него разворачиваются автоматически
- **Первый уровень потомков**: Первый уровень вложенности под активным пунктом также разворачивается
- **Неограниченная вложенность**: Поддержка любого количества уровней вложенности
- **Один запрос к БД**: Оптимизировано для минимального количества запросов
- **Кэширование**: Встроенное кэширование для высокой производительности
- **Django Admin**: Удобное редактирование через стандартную админку Django
- **Template Tag**: Простое использование через `{% draw_menu 'menu_name' %}`
- **Именованные URL**: Поддержка как явных URL, так и именованных URL

### 1. Клонирование и установка

```bash
# Клонируйте репозиторий
git clone <repository-url>
cd django-tree-menu

# Создайте виртуальное окружение
python -m venv venv

# Активируйте виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

### 2. Настройка базы данных

```bash
# Создайте миграции для всех приложений
python manage.py makemigrations

# Если миграции не создались автоматически, создайте их вручную
python manage.py makemigrations tree_menu
python manage.py makemigrations demo

# Примените миграции
python manage.py migrate

# Создайте суперпользователя (если еще не создан)
python manage.py createsuperuser

# Создайте демо-данные
python manage.py create_demo_menu
```

### 3. Запуск

```bash
python manage.py runserver
```

Откройте http://127.0.0.1:8000/ для просмотра демо-страниц.

## 📁 Структура проекта

```
django-tree-menu/
├── config/                 # Настройки проекта
│   ├── settings.py        # Основные настройки Django
│   ├── urls.py            # Главные URL-маршруты
│   ├── wsgi.py            # WSGI конфигурация
│   └── asgi.py            # ASGI конфигурация
├── apps/                   # Приложения
│   ├── tree_menu/         # Основное приложение меню
│   │   ├── models.py      # Модели Menu и MenuItem
│   │   ├── admin.py       # Админка Django
│   │   ├── services.py    # Бизнес-логика
│   │   ├── templatetags/  # Template tags
│   │   └── templates/     # Шаблоны меню
│   └── demo/              # Демо-приложение
│       ├── views.py       # Views для демо-страниц
│       ├── urls.py        # URL-маршруты демо
│       └── templates/     # Шаблоны страниц
├── manage.py              # Django management
├── requirements.txt       # Зависимости
└── README.md             # Документация
```

## 🛠️ Использование

### 1. Создание меню через админку

1. Откройте http://127.0.0.1:8000/admin/
2. Войдите с созданными учетными данными
3. Создайте новое меню в разделе "Меню"
4. Добавьте пункты меню с нужной иерархией

### 2. Отображение в шаблоне

```html
{% load menu_tags %}

<!-- Отображение главного меню -->
{% draw_menu 'main_menu' %}

<!-- Отображение дополнительного меню -->
{% draw_menu 'secondary_menu' %}
```

### 3. Настройка моделей

```python
from apps.tree_menu.models import Menu, MenuItem

# Создание меню
menu = Menu.objects.create(
    name='my_menu',
    description='Мое меню'
)

# Создание пункта меню
item = MenuItem.objects.create(
    menu=menu,
    title='Главная',
    url='/',
    order=1
)

# Создание подпункта
subitem = MenuItem.objects.create(
    menu=menu,
    parent=item,
    title='Подраздел',
    url='/subsection/',
    order=1
)
```

## 🎯 Технические требования

- **Django**: 5.0+
- **Python**: 3.8+
- **База данных**: SQLite (по умолчанию), поддерживаются все БД Django
- **Кэширование**: LocMemCache (по умолчанию)

## 🔧 Архитектура

### Модели

- **Menu**: Основная модель меню
- **MenuItem**: Пункт меню с поддержкой иерархии

### Сервисы

- **MenuService**: Получение данных меню с кэшированием
- **MenuRenderer**: Рендеринг HTML меню

### Template Tags

- **draw_menu**: Основной template tag для отображения меню

## 📊 Производительность

- **1 запрос к БД** на отрисовку каждого меню
- **Кэширование** на 5 минут
- **prefetch_related** для оптимизации запросов
- **Автоматическое разворачивание** без дополнительных запросов

## 🎨 Кастомизация

### CSS стили

Меню использует CSS классы для стилизации:
- `.tree-menu` - основной контейнер
- `.menu-item` - пункт меню
- `.menu-item.active` - активный пункт
- `.menu-item.expanded` - развернутый пункт
- `.submenu` - подменю

### JavaScript

Встроенный JavaScript для интерактивности:
- Клик по стрелке разворачивает/сворачивает подменю
- Плавные анимации

## 📋 Демо-страницы

- **Главная**: http://127.0.0.1:8000/
- **О нас**: http://127.0.0.1:8000/about/
- **Услуги**: http://127.0.0.1:8000/services/
- **Продукты**: http://127.0.0.1:8000/products/
- **Контакты**: http://127.0.0.1:8000/contact/
- **Блог**: http://127.0.0.1:8000/blog/
- **Новости**: http://127.0.0.1:8000/news/
- **FAQ**: http://127.0.0.1:8000/faq/

## 🔐 Доступ к админке

- **URL**: http://127.0.0.1:8000/admin/
- **Логин**: admin
- **Пароль**: admin (или тот, который вы указали при создании)

## ⚠️ Возможные проблемы

### Ошибка "No module named 'apps'"
Убедитесь, что вы находитесь в корневой папке проекта при запуске команд.

### Ошибка "no such table: tree_menu_menu"
Эта ошибка возникает, если миграции не были применены. Выполните:
```bash
python manage.py makemigrations tree_menu
python manage.py migrate
```

### Ошибка миграций
Если возникают проблемы с миграциями, удалите папку `migrations/` и создайте заново:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Проблемы с правами доступа
На Linux/Mac может потребоваться:
```bash
chmod +x manage.py
```
### Визуал
<img width="1280" height="600" alt="image" src="https://github.com/user-attachments/assets/5e98a55d-7b94-417c-aec1-94833cd2c57e" />

<img width="1383" height="506" alt="image" src="https://github.com/user-attachments/assets/8934bcbc-13b6-4df8-ae46-be37bb40d561" />


