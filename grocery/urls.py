# grocery/urls.py
from django.urls import path
from .views import add_to_grocery_list

urlpatterns = [
    path('add/', add_to_grocery_list, name='add_to_grocery_list'),
#     path('list/', grocery_list, name='grocery_list'),
]
