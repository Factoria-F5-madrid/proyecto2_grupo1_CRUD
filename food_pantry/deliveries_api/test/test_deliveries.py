import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.beneficiary import beneficiaries
from common.test.fixtures.delivery import (
    deliveries, 
    delivery_post_payload, 
    delivery_payload_missing_address, 
    delivery_payload_update_address
)


class TestDeliveries:
    end_point = "/food_pantry/api/v1/deliveries/"
    
    # Get all deliveries
    @pytest.mark.django_db
    def test_get_deliveries_returns_ok(self, api_client, deliveries):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a delivery    
    @pytest.mark.django_db
    def test_push_delivery_returns_created(self, api_client, beneficiaries, delivery_post_payload):
        response = api_client.post(self.end_point, delivery_post_payload)
        
        assert response.data.get('delivery_date') == delivery_post_payload.get('delivery_date')
        assert response.data.get('address') == delivery_post_payload.get('address')
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create delivery with bad data    
    @pytest.mark.django_db
    def test_post_delivery_with_missing_address_returns_bad_request(self, api_client, delivery_payload_missing_address):
        response = api_client.post(self.end_point, delivery_payload_missing_address)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single Delivery
    @pytest.mark.django_db
    def test_get_delivery_returns_ok(self, api_client, deliveries):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == deliveries[1].id
        assert response.data.get('delivery_date') == deliveries[1].delivery_date
        assert response.data.get('address') == deliveries[1].address
        assert response.status_code == status.HTTP_200_OK
        
    # Get delivery. Delivery  does not exist
    @pytest.mark.django_db
    def test_get_delivery_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update delivery    
    # @pytest.mark.django_db
    # def test_put_delivery_returns_ok(self, api_client, deliveries, delivery_payload_update_address):
    #     response = api_client.put(self.end_point + "1", delivery_payload_update_address)
        
    #     assert response.data.get('address') == delivery_payload_update_address.get('address')
    #     assert response.status_code == status.HTTP_200_OK
        
    # Update delivery. Delivery does not exist
    @pytest.mark.django_db
    def test_put_non_existing_delivery_returns_bad_request(self, api_client, delivery_payload_update_address):
        response = api_client.put(self.end_point + "1", delivery_payload_update_address)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete delivery
    @pytest.mark.django_db
    def test_delete_delivery_returns_ok(self, api_client, deliveries):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Delete Beneficiary. Beneficiary des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_delivery_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST