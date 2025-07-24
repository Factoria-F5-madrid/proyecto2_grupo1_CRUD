import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.beneficiary import (
    beneficiaries, 
    delivery_products_post_payload, 
    beneficiary_payload_missing_name, 
    beneficiary_payload_update_name
)


class TestBeneficiaries:
    end_point = "/food_pantry/api/v1/beneficiaries/"
    
    # Get all beneficiaries
    @pytest.mark.django_db
    def test_get_benficiaries_returns_ok(self, api_client, beneficiaries):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a beneficiary    
    @pytest.mark.django_db
    def test_push_beneficiary_returns_created(self, api_client, delivery_products_post_payload):
        response = api_client.post(self.end_point, delivery_products_post_payload)
        
        assert response.data.get('name') == delivery_products_post_payload.get('name')
        assert response.data.get('address') == delivery_products_post_payload.get('address')
        assert response.data.get('contact_info') == delivery_products_post_payload.get('contact_info')
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create benficiary with bad data    
    @pytest.mark.django_db
    def test_post_donor_with_missing_name_returns_bad_request(self, api_client, beneficiary_payload_missing_name):
        response = api_client.post(self.end_point, beneficiary_payload_missing_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single Benficiary
    @pytest.mark.django_db
    def test_get_beneficiary_returns_ok(self, api_client, beneficiaries):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == beneficiaries[1].id
        assert response.data.get('name') == beneficiaries[1].name
        assert response.data.get('address') == beneficiaries[1].address
        assert response.data.get('contact_info') == beneficiaries[1].contact_info
        assert response.status_code == status.HTTP_200_OK
        
    # Get beneficiarie. Beneficiary does not exist
    @pytest.mark.django_db
    def test_get_beneficiary_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update beneficiary    
    @pytest.mark.django_db
    def test_put_donor_returns_ok(self, api_client, beneficiaries, beneficiary_payload_update_name):
        response = api_client.put(self.end_point + "1", beneficiary_payload_update_name)
        
        assert response.data.get('name') == beneficiary_payload_update_name.get('name')
        assert response.status_code == status.HTTP_200_OK
        
    # Update Beneficiary. Benficiary does not exist
    @pytest.mark.django_db
    def test_put_non_existing_beneficiary_returns_bad_request(self, api_client, beneficiary_payload_update_name):
        response = api_client.put(self.end_point + "1", beneficiary_payload_update_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete beneficiary
    @pytest.mark.django_db
    def test_delete_beneficiary_returns_ok(self, api_client, beneficiaries):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Delete Beneficiary. Beneficiary des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_beneficiary_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST