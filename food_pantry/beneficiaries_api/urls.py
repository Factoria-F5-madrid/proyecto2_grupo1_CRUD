from django.urls import path

from .views.beneficiaries_view import BeneficiariesView
from .views.beneficiary_by_id_view import BeneficiaryByIdView   

base_url = ""

urlpatterns = [
    path(base_url, BeneficiariesView.as_view(), name="beneficiaries"),
    path(base_url + '<int:beneficiary_id>', BeneficiaryByIdView.as_view(), name="beneficiary"),
]

