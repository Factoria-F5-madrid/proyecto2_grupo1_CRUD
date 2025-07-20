from rest_framework import serializers

from .models import Volunteer

class VolunteerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['name', 'email']
        

class VolunteerResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'name', 'email']
        