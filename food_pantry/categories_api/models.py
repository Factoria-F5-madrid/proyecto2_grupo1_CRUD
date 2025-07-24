from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    """Represents a category assigned to donated products."""
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

