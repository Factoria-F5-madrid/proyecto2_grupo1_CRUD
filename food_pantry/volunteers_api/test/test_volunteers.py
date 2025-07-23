import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.volunteer import (
    volunteers,
    volunteer_post_payload,
    volunteer_payload_update_name,
    volunteer_payload_missing_name
)

class TestVolunteers:
    end_point = "/food_pantry/api/v1/volunteers/"
    
    # Get all volunteers
    @pytest.mark.django_db
    def test_get_volunteers_returns_ok(self, api_client, volunteers):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a volunteer    
    @pytest.mark.django_db
    def test_push_volunteer_returns_created(self, api_client, volunteer_post_payload):
        response = api_client.post(self.end_point, volunteer_post_payload)
        
        assert response.data.get('name') == volunteer_post_payload.get('name')
        assert response.data.get('email') == volunteer_post_payload.get('email')
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create volunteer with bad data    
    @pytest.mark.django_db
    def test_post_volunteer_with_missing_name_returns_bad_request(self, api_client, volunteer_payload_missing_name):
        response = api_client.post(self.end_point, volunteer_payload_missing_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single volunteer
    @pytest.mark.django_db
    def test_get_volunteer_returns_ok(self, api_client, volunteers):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == volunteers[1].id
        assert response.data.get('name') == volunteers[1].name
        assert response.data.get('email') == volunteers[1].email
        assert response.status_code == status.HTTP_200_OK
        
    # Get volunteer. Volunteer does not exist
    @pytest.mark.django_db
    def test_get_volunteer_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update volunteer    
    @pytest.mark.django_db
    def test_put_volunteer_returns_ok(self, api_client, volunteers, volunteer_payload_update_name):
        response = api_client.put(self.end_point + "1", volunteer_payload_update_name)
        
        assert response.data.get('name') == volunteer_payload_update_name.get('name')
        assert response.status_code == status.HTTP_200_OK
        
    # Update volunteer. Volunteer does not exist
    @pytest.mark.django_db
    def test_put_non_existing_volunteer_returns_bad_request(self, api_client, volunteer_payload_update_name):
        response = api_client.put(self.end_point + "1", volunteer_payload_update_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete volunteer
    @pytest.mark.django_db
    def test_delete_volunteer_returns_ok(self, api_client, volunteers):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Delete volunteer. Volunteer does not exist
    @pytest.mark.django_db
    def test_delete_non_existing_volunteer_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST