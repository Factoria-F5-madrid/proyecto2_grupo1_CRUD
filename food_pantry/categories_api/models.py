from django.db import models

class Donors(models.Model):
    """
    Modelo para representar un donante en el banco de alimentos.
    """
    name = models.CharField(max_length=180)
    type= models.CharField(max_length=180)
    contact = models.CharField(max_length=180)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Modelo para representar una categoría de alimentos o artículos.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Nombre único de la categoría.")
    description = models.TextField(blank=True, null=True, help_text="Descripción detallada de la categoría.")

    class Meta:
        verbose_name_plural = "Categories" # Para que en el admin se vea "Categories" y no "Categorys"

    def __str__(self):
        return self.name