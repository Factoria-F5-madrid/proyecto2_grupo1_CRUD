from django.urls import path  

from .views.categories_view import CategoryListCreateView, CategoryDetailView  

base_url=""  
    
urlpatterns = [  
    path(base_url, CategoryListCreateView.as_view(), name="categories"),  
    path(base_url + '<int:pk>', CategoryDetailView.as_view(), name="category"),  
]