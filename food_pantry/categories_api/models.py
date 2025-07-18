from django.db import models

# Create your models here.
class Category(models.Model):
    """Represents a category assigned to donated products."""
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

