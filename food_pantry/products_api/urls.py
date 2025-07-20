# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.products_view import ProductsView
from .views.products_by_id_view import ProductsByIdView

base_url = ""

urlpatterns = [
    path(base_url, ProductsView.as_view(), name="products"),
    path(base_url + '<int:id>', ProductsByIdView.as_view(), name="product"),
]
