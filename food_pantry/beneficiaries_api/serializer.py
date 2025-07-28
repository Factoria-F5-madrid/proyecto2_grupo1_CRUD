from rest_framework import serializers
from .models import Beneficiary

class BeneficiaryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['name', 'address', 'contact_info']
        

class BeneficiaryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = ['id', 'name', 'address', 'contact_info']