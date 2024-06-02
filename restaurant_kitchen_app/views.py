from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Menu, meal_types


class MenuList(generic.ListView):
    queryset = Menu.objects.order_by('-date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = meal_types
        return context


class MenuDetail(generic.DetailView):
    model = Menu
    template_name = 'menu_details.html'
