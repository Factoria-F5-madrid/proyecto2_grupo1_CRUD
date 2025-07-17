# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.donors_view import DonorsView
from .views.donors_by_id_view import DonorsByIdView

base_url=""
    
urlpatterns = [
    path(base_url, DonorsView.as_view(), name="donors"),
    path(base_url + '<int:id>', DonorsByIdView.as_view(), name="donor"),
]
    