from django.db import models

# Create your models here.
class Volunteer(models.Model):
    """Represents a volunteer who participates in deliveries."""
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name