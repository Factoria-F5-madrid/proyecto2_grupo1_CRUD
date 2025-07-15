# In here we place the URLs for the web application
from django.urls import path

from ..views.food_pantry_app_home_view import FoodPantryAppHomeView

    
urlpatterns = [
    path('', FoodPantryAppHomeView.as_view())
]
    