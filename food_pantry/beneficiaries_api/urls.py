from django.urls import path

from .views.beneficiaries_view import BeneficiariesView
from .views.beneficiaries_by_id_view import BeneficiariesByIdView

base_url = ""

urlpatterns = [
    path(base_url, BeneficiariesView.as_view(), name="beneficiaries"),
    path(base_url + '<int:id>', BeneficiariesByIdView.as_view(), name="beneficiary"),
]
