# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.products_view import ProductsView
from .views.product_by_id_view import ProductByIdView

base_url = ""

urlpatterns = [
    path(base_url, ProductsView.as_view(), name="products"),
    path(base_url + '<int:product_id>', ProductByIdView.as_view(), name="product"),
]


    