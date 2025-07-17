# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.volunteer_deliveries_view import VolunteerDeliveriesView
from .views.volunteer_delivery_by_id_view import VolunteerDeliveryByIdView

base_url = ""

urlpatterns = [
    path(base_url, VolunteerDeliveriesView.as_view(), name="volunteer_deliveries"),
    path(base_url + '<int:delivery_id>', VolunteerDeliveryByIdView.as_view(), name="volunteer_delivery"),
]

