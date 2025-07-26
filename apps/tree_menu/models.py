"""
Модели для древовидного меню
"""
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class Menu(models.Model):
    """Модель меню"""
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель пункта меню"""
    menu = models.ForeignKey(
        Menu, 
        on_delete=models.CASCADE, 
        related_name='items',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children',
        verbose_name='Родительский пункт'
    )
    title = models.CharField('Заголовок', max_length=100)
    url = models.CharField('URL', max_length=200, blank=True)
    named_url = models.CharField('Именованный URL', max_length=100, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order', 'title']
        unique_together = [['menu', 'parent', 'title']]

    def __str__(self):
        return f"{self.title} ({self.menu.name})"

    def clean(self):
        """Валидация: URL или named_url должны быть заполнены"""
        if not self.url and not self.named_url:
            raise ValidationError('Необходимо указать URL или именованный URL')

    def get_url(self):
        """Получить URL пункта меню"""
        if self.url:
            return self.url
        elif self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return '#'
        return '#'

    def get_ancestors(self):
        """Получить всех предков"""
        ancestors = []
        current = self.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return list(reversed(ancestors))

    def get_descendants(self):
        """Получить всех потомков"""
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            descendants.extend(child.get_descendants())
        return descendants

    def get_siblings(self):
        """Получить соседние пункты"""
        if self.parent:
            return self.parent.children.exclude(id=self.id)
        else:
            return self.menu.items.filter(parent=None).exclude(id=self.id) 