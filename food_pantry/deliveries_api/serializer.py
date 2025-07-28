from rest_framework import serializers

from deliveries_api.models import Delivery

class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['delivery_date', 'beneficiary', 'address']
        extra_kwargs = {
            'address': {'required': False}
        }


class DeliveryResponseSerializer(serializers.ModelSerializer):
    beneficiary_name = serializers.CharField(source='beneficiary.name', read_only=True)

    class Meta:
        model = Delivery
        fields = ['id', 'delivery_date', 'beneficiary', 'beneficiary_name', 'address']

        
