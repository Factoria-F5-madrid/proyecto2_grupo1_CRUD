from django.db import models
 
class Donor(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    class Meta:
        verbose_name_plural = 'Donors'
    
    DONOR_TYPES = [
        ("individual", "Individual"),
        ("institución", "Institución")
    ]

    name = models.CharField(max_length=180)
    type= models.CharField(max_length=20, choices=DONOR_TYPES)
    contact = models.CharField(max_length=180)
    anonymous = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
