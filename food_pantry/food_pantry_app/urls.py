# In here we place the URLs for the web application
from django.urls import path

from .views.home_view import HomeView
    
urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
]
    