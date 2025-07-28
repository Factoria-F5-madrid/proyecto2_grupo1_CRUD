import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.volunteer_deliveries import (
    volunteer_deliveries,
    volunteer_delivery_post_payload,
    volunteer_delivery_payload_missing_delivery,
    volunteer_delivery_payload_update_delivery
)
from common.test.fixtures.volunteer import volunteers
from common.test.fixtures.delivery import deliveries
from common.test.fixtures.beneficiary import beneficiaries

class TestVolunteerDeliveries:
    end_point = "/food_pantry/api/v1/volunteer_deliveries/"
    
    # Get all volunteer_deliveries
    @pytest.mark.django_db
    def test_get_volunteer_deliveries_returns_ok(self, api_client, volunteer_deliveries, volunteers, deliveries, beneficiaries):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a volunteer delivery
    @pytest.mark.django_db
    def test_push_volunteer_deliveries_returns_created(self, api_client, volunteer_delivery_post_payload, volunteers, deliveries):
        response = api_client.post(self.end_point, volunteer_delivery_post_payload)
        
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create volunteer_deliveries with bad data    
    @pytest.mark.django_db
    def test_post_volunteer_deliveries_with_missing_name_returns_bad_request(self, api_client, volunteer_delivery_payload_missing_delivery):
        response = api_client.post(self.end_point, volunteer_delivery_payload_missing_delivery)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single volunteer_deliveries
    @pytest.mark.django_db
    def test_get_volunteer_deliveries_returns_ok(self, api_client, volunteer_deliveries, volunteers, deliveries):
        response = api_client.get(self.end_point + "2")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Get volunteer_deliveries, but it does not exist
    @pytest.mark.django_db
    def test_get_volunteer_deliveries_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update volunteer_deliveries    
    # @pytest.mark.django_db
    # def test_put_volunteer_deliveries_returns_ok(self, api_client, volunteer_deliveries, volunteers, deliveries, volunteer_delivery_payload_update_delivery):
    #     response = api_client.put(self.end_point + "1", volunteer_delivery_payload_update_delivery)
        
    #     assert response.status_code == status.HTTP_200_OK
        
    # Update volunteer_deliveries. Donor does not exist
    @pytest.mark.django_db
    def test_put_non_existing_volunteer_deliveries_returns_bad_request(self, api_client, volunteer_delivery_payload_update_delivery):
        response = api_client.put(self.end_point + "1", volunteer_delivery_payload_update_delivery)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete volunteer_deliveries
    @pytest.mark.django_db
    def test_delete_volunteer_deliveries_returns_ok(self, api_client, volunteer_deliveries, volunteers, deliveries):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    # Delete volunteer_deliveries. Donor des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_volunteer_deliveries_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST