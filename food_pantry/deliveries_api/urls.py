# In here we place the URLs for the API (Swagger)
from django.urls import path


from .views.deliveries_view import DeliveriesView
from .views.deliveries_by_id_view import DeliveriesByIdView

base_url = ""

urlpatterns = [
    path(base_url, DeliveriesView.as_view(), name="deliveries"),
    path(base_url + '<int:delivery_id>', DeliveriesByIdView.as_view(), name="delivery"),
]



