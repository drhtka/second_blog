# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models

# метки для нашей статьи
class Category(models.Model):
    """Класс категории статей

    """
    title = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Tag(models.Model):
    """Класс тегов статей

    """
    title = models.CharField('Тег', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title

class News(models.Model):
    """класс новостей

    """
    user = models.ForeignKey(User,
                             verbose_name='Автор',
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL,
                                 null=True)
    title = models.CharField('Заголовок', max_length=100)
    text_min = models.TextField('Мини Описание', max_length=350)
    text = models.TextField('Текст статьи')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    description = models.CharField('Описание', max_length=100)
    keywords = models.CharField('Ключевые слова', max_length=50)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Coments(models.Model):
    """Класс комментариев к новостям

    """
    user = models.ForeignKey(
        User,
        verbose_name="Пользователи",
        on_delete=models.CASCADE
    )
    new = models.ForeignKey(
        News,
        verbose_name='Новость',
        on_delete=models.CASCADE
    )

    text = models.TextField('Комментарий')
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField('Модерация', default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return "{}".format(self.user)
