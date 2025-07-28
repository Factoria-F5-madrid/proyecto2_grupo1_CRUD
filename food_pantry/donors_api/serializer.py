from rest_framework import serializers

from .models import Donor

class DonorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['name', 'type', 'contact', 'anonymous']
        

class DonorResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id', 'name', 'type', 'contact', 'anonymous']
        