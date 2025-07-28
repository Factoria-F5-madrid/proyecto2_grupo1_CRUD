import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.donor import (
    donors, donor_post_payload, donor_payload_missing_name, 
    donor_payload_update_name
)

class TestDonors:
    end_point = "/food_pantry/api/v1/donors/"
    
    # Get all donors
    @pytest.mark.django_db
    def test_get_donors_returns_ok(self, api_client, donors):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a donor    
    @pytest.mark.django_db
    def test_push_donor_returns_created(self, api_client, donor_post_payload):
        response = api_client.post(self.end_point, donor_post_payload)
        
        assert response.data.get('name') == donor_post_payload.get('name')
        assert response.data.get('type') == donor_post_payload.get('type')
        assert response.data.get('contact') == donor_post_payload.get('contact')
        assert response.data.get('anonymous') ==  bool(donor_post_payload.get('anonymous'))
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create donor with bad data    
    @pytest.mark.django_db
    def test_post_donor_with_missing_name_returns_bad_request(self, api_client, donor_payload_missing_name):
        response = api_client.post(self.end_point, donor_payload_missing_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single donor
    @pytest.mark.django_db
    def test_get_donor_returns_ok(self, api_client, donors):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == donors[1].id
        assert response.data.get('name') == donors[1].name
        assert response.data.get('type') == donors[1].type
        assert response.data.get('contact') == donors[1].contact
        assert response.data.get('anonymous') == donors[1].anonymous
        assert response.status_code == status.HTTP_200_OK
        
    # Get donor. Donor does not exist
    @pytest.mark.django_db
    def test_get_donor_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update donor    
    @pytest.mark.django_db
    def test_put_donor_returns_ok(self, api_client, donors, donor_payload_update_name):
        response = api_client.put(self.end_point + "1", donor_payload_update_name)
        
        assert response.data.get('name') == donor_payload_update_name.get('name')
        assert response.status_code == status.HTTP_200_OK
        
    # Update donor. Donor does not exist
    @pytest.mark.django_db
    def test_put_non_existing_donor_returns_bad_request(self, api_client, donor_payload_update_name):
        response = api_client.put(self.end_point + "1", donor_payload_update_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete donor
    @pytest.mark.django_db
    def test_delete_donor_returns_ok(self, api_client, donors):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Delete donor. Donor des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_donor_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST