from django.db import models
from donors_api.models import Donor
from categories_api.models import Category


# Create your models here.
class Product(models.Model):
    """Represents a donated product with donor and category information."""
    name = models.CharField(max_length=180)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField(null=True, blank=True)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name='donor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f"{self.name} ({self.quantity})"