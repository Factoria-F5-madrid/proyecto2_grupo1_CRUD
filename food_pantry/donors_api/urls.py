# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.donors_bulk_view import DonorsBulkView
from .views.donors_single_view import DonorsSingleView

base_url=""
    
urlpatterns = [
    path(base_url, DonorsBulkView.as_view(), name="donors"),
    path(base_url + '<int:donor_id>', DonorsSingleView.as_view(), name="donor"),
]
    