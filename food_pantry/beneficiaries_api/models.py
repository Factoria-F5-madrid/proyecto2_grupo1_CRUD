from django.db import models

# Create your models here.
from django.db import models

class Beneficiary(models.Model):
    """Represents a recipient of food deliveries."""
    name = models.CharField(max_length=180)
    address = models.TextField(blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name