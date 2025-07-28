import pytest
from rest_framework import status
from common.test.fixtures.api import api_client
from common.test.fixtures.delivery_products import (
    delivery_products,
    delivery_products_post_payload,
    delivery_products_payload_missing_quantity,
    delivery_products_payload_update_quantity
)
from common.test.fixtures.product import products
from common.test.fixtures.delivery import deliveries
from common.test.fixtures.beneficiary import beneficiaries
from common.test.fixtures.donor import donors
from common.test.fixtures.category import categories


class TestDeliveryProducts:
    end_point = "/food_pantry/api/v1/delivery_products/"
    
    # Get all delivery products
    @pytest.mark.django_db
    def test_get_deliveries_products_returns_ok(
        self, api_client, 
        delivery_products, 
        products, 
        beneficiaries,
        deliveries, 
        donors,
        categories
    ):
        response = api_client.get(self.end_point + "?confirm=true")
    
        assert len(response.data) == 2
        assert response.status_code == status.HTTP_200_OK
    
    # Create a delivery product    
    @pytest.mark.django_db
    def test_push_deliveries_products_returns_created(self, api_client, products, deliveries, delivery_products_post_payload):
        response = api_client.post(self.end_point, delivery_products_post_payload)
        
        assert response.data.get('quantity_delivered') == delivery_products_post_payload.get('quantity_delivered')
        assert response.status_code == status.HTTP_201_CREATED
    
    # Create delivery product with bad data    
    @pytest.mark.django_db
    def test_post_delivery_product_with_missing_quantity_returns_bad_request(self, api_client, delivery_products_payload_missing_quantity):
        response = api_client.post(self.end_point, delivery_products_payload_missing_quantity)
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    # Get single delivery product
    @pytest.mark.django_db
    def test_get_delivery_product_returns_ok(
        self, api_client,
        delivery_products,
        products,
        deliveries,
        donors,
        beneficiaries,
        categories
        ):
        response = api_client.get(self.end_point + "2")
        
        assert response.data.get('id') == delivery_products[1].id
        assert response.data.get('quantity_delivered') == delivery_products[1].quantity_delivered
        assert response.status_code == status.HTTP_200_OK
        
    # Get delivery product. Delivery product does not exist
    @pytest.mark.django_db
    def test_get_deliveries_products_does_not_exist_returns_bad_request(self, api_client):
        response = api_client.get(self.end_point + "1")
    
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    # Update delivery product    
    @pytest.mark.django_db
    def test_put_donor_returns_ok(self, api_client, delivery_products, products, deliveries, delivery_products_payload_update_quantity):
        response = api_client.put(self.end_point + "1", delivery_products_payload_update_quantity)
        
        assert response.data.get('quantity_provided') == delivery_products_payload_update_quantity.get('quantity_provided')
        assert response.status_code == status.HTTP_200_OK
        
    # Update delivery product. Delivery product does not exist
    @pytest.mark.django_db
    def test_put_non_existing_deliveries_product_returns_bad_request(self, api_client, delivery_products_payload_update_quantity):
        response = api_client.put(self.end_point + "1", delivery_products_payload_update_quantity)
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    # Delete delivery product
    @pytest.mark.django_db
    def test_delete_deliveries_product_returns_ok(self, api_client, delivery_products, products, deliveries):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_204_NO_CONTENT
        
    # Delete delivery product. Delivery product des not exist
    @pytest.mark.django_db
    def test_delete_non_existing_deliveries_product_returns_bad_request(self, api_client):
        response = api_client.delete(self.end_point + "1")
        
        assert response.status_code == status.HTTP_404_NOT_FOUND