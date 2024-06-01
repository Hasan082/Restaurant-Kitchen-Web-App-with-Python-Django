from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('menu/<int:menu_id>/', views.MenuDetail.as_view(), name='menu_details'),
]