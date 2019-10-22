# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Ticket
from .forms import AddTicketForms
"""
class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Class of Django')

class MyTemplateView(TemplateView):

    template_name = 'add_ticket.html'

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context['text'] = 'Hi world!'
        return context
        
""" # test

class AddTicket(CreateView):
    """Добавление тикета
    """
    model = Ticket
    form_class = AddTicketForms
    template_name = 'add_ticket.html'
    #  при успешном добавлении куда будет добавляться пользователь

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()# проверка на валидность
        return redirect('/ticket/add-ticket/')

    def succes_url(self):
        return redirect('/add-ticket/')# куда редиректить когда мы сделам что либо на наш url

