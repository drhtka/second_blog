# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Class of Django')

class MyTemplateView(TemplateView):

    template_name = 'add_ticket.html'

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context['text'] = 'Hi world!'
        return context