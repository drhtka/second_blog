# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .models import Ticket
from .forms import AddTicketForms

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

class ListTicket(ListView):
    """Список тикетов пользователя
    """
    model = Ticket
    queryset = Ticket.objects.all()
    context_object_name = 'tickets'
    template_name = 'list-ticket.html'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)# выводит тикет данного пользователя

class UpdateTicket(UpdateView):
    """Редактирование тикета
    """
    model = Ticket
    form_class = AddTicketForms
    template_name = 'update_ticket.html' # можно было list-ticket

    def get_success_url(self):
        return reverse('list-ticket')