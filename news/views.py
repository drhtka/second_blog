# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Coments
from news.forms import CommentForm
from datetime import datetime, timedelta

def news_list(request):
    """Вывод всех новостей

    """
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})


def new_single(request, pk):
    """Вывод полной статьи
    """

    new = get_object_or_404(News, id=pk)
    comment = Coments.objects.filter(new=pk, moderation=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid: # нам нужно присвоить к тому user который сейчас на сайте добавил коментарий
            form = form.save(commit=False) # для это пиостанавливаем сохранение
            form.user = request.user # присваиваем запросить пользователя который сейчас на сайте
            form.new = new
            form.save()  # сохраняем нашу форму
            return redirect(new_single, pk)# чтоб вернулась страница с полем ввода комментария
    else:
        form = CommentForm()
    return render(request, 'new_singl.html', {'new': new,
                                              'comment': comment,
                                              'form': form})

def news_filter(request, pk):
    """Фильтр статей по дате
    """
    news = News.objects.all()
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60*24*7)#определим сегодняшнюю дату() отнимем в  минуты*сутки дни недели
        news = news.filter(created__gte=now)# все наши статьи, по полю created  определим созданные наши статьи

    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60*24*30)
        news = news.filter(created__gte=now)

    elif pk == 3:
        news = news

    return render(request, 'news_list.html', {'news': news})