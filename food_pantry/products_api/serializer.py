from rest_framework import serializers

from .models import Product

class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'expiration_date', 'donor_id', 'category_id']
        

class ProductResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'expiration_date', 'donor_id', 'category_id']
