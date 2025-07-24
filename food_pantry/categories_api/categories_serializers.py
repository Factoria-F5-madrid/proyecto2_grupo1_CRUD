from rest_framework import serializers

from .models import Categories

class CategoriesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name_food', 'type', 'description', 'unit', ' expiration_date', 'quantity', 'donor']
        

class CategoriesResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'type', 'expiration_date', 'donor', 'quantity', 'unit', 'description',]
        read_only_fields = ['id'] # El 'id' se genera automáticamente