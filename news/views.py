# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from news.models import News

def news_list(request):
    """Вывод всех новостей

    """
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})


def new_single(request, pk):
    """Вывод полной статьи

    """
    new = get_object_or_404(News, id=pk)
    return render(request, 'new_singl.html', {'new': new})