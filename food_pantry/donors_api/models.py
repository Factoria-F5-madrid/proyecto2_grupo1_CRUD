from django.db import models

class Donor(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    
    name = models.CharField(max_length=180)
    type= models.CharField(max_length=180)
    contact = models.CharField(max_length=180)
    anonymous = models.BooleanField(default=False)
    
