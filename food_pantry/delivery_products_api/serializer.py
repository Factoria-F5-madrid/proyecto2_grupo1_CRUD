from rest_framework import serializers
from .models import DeliveryProduct

class DeliveryProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProduct
        fields = ['delivery', 'product', 'quantity_delivered']
        

class DeliveryProductResponseSerializer(serializers.ModelSerializer):
    
    """Serializer for DeliveryProduct model to return specific fields."""

    product_name = serializers.CharField(source='product.name', read_only=True)
    delivery_date = serializers.DateField(source='delivery.delivery_date', read_only=True)

    class Meta:
        model = DeliveryProduct
        fields = ['id', 'delivery', 'delivery_date', 'product', 'product_name', 'quantity_delivered']
