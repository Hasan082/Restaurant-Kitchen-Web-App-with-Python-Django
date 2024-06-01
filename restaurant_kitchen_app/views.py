from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Menu

class MenuList(generic.ListView):
    queryset = Menu.objects.order_by('-date_created')
    template_name = 'index.html'

    def get_context_data(self):
        context = {
            'Dinner': 'Dinner',
            'Lunch': 'Lunch',
            'Breakfast': 'Breakfast',
            'Dessert': 'Dessert',
            'Drinks': 'Drinks',
            'Salads': 'Salads',
        }
        return context


class MenuDetail(generic.DetailView):
    model = Menu
    template_name = 'menu_details.html'
