from rest_framework import serializers

from .models import Category

class CategoriesRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        

class CategoriesResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description',]
        read_only_fields = ['id'] 