# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.donors_view import DonorsView
from .views.donors_by_donor_id_view import DonorsByDonorIdView

base_url=""
    
urlpatterns = [
    path(base_url, DonorsView.as_view(), name="donors"),
    path(base_url + '<int:donor_id>', DonorsByDonorIdView.as_view(), name="donor"),
]
    