# foodwaste/recipes/urls.py
from django.urls import path
from .views import generate_recipe,track_expiration,delete_perishable_item

urlpatterns = [
    path('generate/', generate_recipe, name='generate_recipe'),
    path('track/', track_expiration, name='track_expiration'),
    path('delete/<int:item_id>/', delete_perishable_item, name='delete_perishable_item'),
]
