from django.urls import path


# In here we place the URLs for the API (Swagger)
from .vews.categories_view import CategoriesView
from .views.categories_by_category_id_view import CategoriesByCategoryIdView


base_url=""

urlpatterns = [
    path(base_url, CategoriesView.as_view(), name="categories"),
    path(base_url + '<int:category_id>', CategoriesByCategoryIdView.as_view(), name="category"),
]

