from django.db import models
from beneficiaries_api.models import Beneficiary

# Create your models here.
class Delivery(models.Model):
    """Represents a delivery made to a beneficiary."""
    delivery_date = models.DateField()
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)

    def __str__(self):
        return f"Delivery to {self.beneficiary.name} on {self.delivery_date}"