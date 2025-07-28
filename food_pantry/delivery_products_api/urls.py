# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.delivery_products_view import DeliveryProductsView
from .views.delivery_product_by_id_view import DeliveryProductByIdView  

base_url = ""

urlpatterns = [
    path(base_url, DeliveryProductsView.as_view(), name="delivery_products"),
    path(base_url + '<int:id>', DeliveryProductByIdView.as_view(), name="delivery_product"),
]