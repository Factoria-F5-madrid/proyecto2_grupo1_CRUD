from rest_framework import serializers

from .models import Donor

class DonorRequest(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['name', 'type', 'contact', 'anonymous']
        

class DonorResponse(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id', 'name', 'type', 'contact', 'anonymous']
        