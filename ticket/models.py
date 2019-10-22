# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class CategoryTicket(models.Model):
    """Категории тикетов
    """
    title = models.CharField('Категория', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'

    def __str__(self):
        return self.title

class Ticket(models.Model):
    """ Класс тикетов
    """

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE)

    category = models.ForeignKey(
        CategoryTicket,
        verbose_name='Категория',
        on_delete=models.CASCADE)

    title = models.CharField('Тема', max_length=100)
    text = models.TextField("Текст письма", max_length=1000)

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'
        db_table = 'ticket'

    def __str__(self):
        return "{}, {}".format(self.title, self.user)
