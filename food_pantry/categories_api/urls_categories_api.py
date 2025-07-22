from django.urls import path

from food_pantry.food_pantry.categories_api.views import category_detail, category_list


# In here we place the URLs for the API (Swagger)
from .views.categories_view import CategoriesView
from .views import CategoriesByCategoryIdView


base_url=""

urlpatterns = [
    path(base_url, CategoriesView.as_view(), name="categories"),
    path(base_url + '<int:category_id>', CategoriesByCategoryIdView.as_view(), name="category"),
    # Endpoint para listar todas las categorías y crear una nueva
    path('categories/', category_list.CategoryList.as_view(), name='category-list'),

    # Endpoint para obtener, actualizar o eliminar una categoría específica
    path('categories/<int:pk>/', category_detail.CategoryDetail.as_view(), name='category-detail'),
]

