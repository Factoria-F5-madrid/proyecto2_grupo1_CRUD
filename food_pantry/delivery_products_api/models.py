from django.db import models
from deliveries_api.models import Delivery
from products_api.models import Product

# Create your models here.
class DeliveryProduct(models.Model):
    class Meta:
        verbose_name_plural = 'Delivery products'
    
    """Represents a specific quantity of a product delivered in a delivery."""
    
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_delivered = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity_delivered} x {self.product.name} for Delivery {self.delivery.id}"