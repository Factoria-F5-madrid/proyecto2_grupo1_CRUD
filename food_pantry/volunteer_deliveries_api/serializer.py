from rest_framework import serializers

from volunteer_deliveries_api.models import VolunteerDelivery

class VolunteerDeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerDelivery
        fields = ['volunteer', 'delivery']
        extra_kwargs = {
            'volunteer': {'required': True},
            'delivery': {'required': True}
        }

class VolunteerDeliveryResponseSerializer(serializers.ModelSerializer):
    volunteer_name = serializers.CharField(source='volunteer.name', read_only=True)
    delivery_id = serializers.IntegerField(source='delivery.id', read_only=True)

    class Meta:
        model = VolunteerDelivery
        fields = ['id', 'volunteer', 'volunteer_name', 'delivery', 'delivery_id']   
  