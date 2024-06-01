from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('meal','description','price', 'meal_type', 'status')
    list_filter = ('meal_type', 'status')
    search_fields = ('meal', 'description')

admin.site.register(Menu, MenuAdmin)
