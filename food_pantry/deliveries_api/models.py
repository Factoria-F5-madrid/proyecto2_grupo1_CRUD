from django.db import models
from beneficiaries_api.models import Beneficiary

# Create your models here.
class Delivery(models.Model):
    class Meta:
        verbose_name_plural = 'Deliveries'
        
    """Represents a delivery made to a beneficiary."""
    delivery_date = models.DateField()
    address = models.CharField(max_length=255, blank=True, null=True)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='deliveries')

    def __str__(self):
        return f"Delivery {self.id} to {self.beneficiary.name} on {self.delivery_date}"

