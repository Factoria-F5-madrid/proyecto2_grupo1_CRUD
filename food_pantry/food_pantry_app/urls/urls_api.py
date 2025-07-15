# In here we place the URLs for the API (Swagger)
from django.urls import path

from ..views.food_pantry_api_donors_view import FoodPantryApiDonorsView

    
urlpatterns = [
    path('donors', FoodPantryApiDonorsView.as_view(), name="donors"),
]
    