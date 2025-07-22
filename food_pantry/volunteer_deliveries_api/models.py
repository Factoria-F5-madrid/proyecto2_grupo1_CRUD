from django.db import models
from volunteers_api.models import Volunteer
from deliveries_api.models import Delivery

# Model to link volunteers with deliveries
class VolunteerDelivery(models.Model):
    """Represents a volunteer assigned to a delivery."""
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.name} - Delivery {self.delivery.id}"

