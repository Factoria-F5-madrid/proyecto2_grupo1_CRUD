import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.donor import donors
from common.test.fixtures.category import categories
from common.test.fixtures.product import (
    products,
    product_post_payload,
    product_payload_update_name,
    product_payload_missing_name
)


class TestBeneficiaries:
    end_point = "/food_pantry/api/v1/products/"
    
    # Get all products
    @pytest.mark.django_db
    def test_get_products_returns_ok(self, api_client, products):
        response = api_client.get(self.end_point)
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a product    
    @pytest.mark.django_db
    def test_push_product_returns_created(self, api_client, donors, categories, product_post_payload):
        response = api_client.post(self.end_point, product_post_payload)
        
        assert response.data.get('name') == product_post_payload.get('name')
        assert response.data.get('quantity') == product_post_payload.get('quantity')
        assert response.data.get('expiration_date') == product_post_payload.get('expiration_date')
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create beproduct with bad data    
    @pytest.mark.django_db
    def test_post_donor_with_missing_name_returns_bad_request(self, api_client, donors, categories, product_payload_missing_name):
        response = api_client.post(self.end_point, product_payload_missing_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single product
    @pytest.mark.django_db
    def test_get_product_returns_ok(self, api_client, products):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == products[1].id
        assert response.data.get('name') == products[1].name
        assert response.data.get('quantity') == products[1].quantity
        assert response.data.get('expiration_date') == products[1].expiration_date
        assert response.status_code == status.HTTP_200_OK
        
    # Get product. Product does not exist
    @pytest.mark.django_db
    def test_get_product_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    # Update product    
    @pytest.mark.django_db
    def test_put_donor_returns_ok(self, api_client, products, product_payload_update_name):
        response = api_client.put(self.end_point + "1", product_payload_update_name)
        
        assert response.data.get('name') == product_payload_update_name.get('name')
        assert response.status_code == status.HTTP_200_OK
        
    # Update product. Product does not exist
    @pytest.mark.django_db
    def test_put_non_existing_product_returns_bad_request(self, api_client, product_payload_update_name):
        response = api_client.put(self.end_point + "1", product_payload_update_name)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Delete product
    @pytest.mark.django_db
    def test_delete_product_returns_ok(self, api_client, products):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_200_OK
        
    # Delete Product. Product des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_product_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST