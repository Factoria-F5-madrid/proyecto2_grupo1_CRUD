import pytest
from delivery_products_api.models import DeliveryProduct
from deliveries_api.models import Delivery
from products_api.models import Product
from common.test.fixtures.delivery import deliveries
from common.test.fixtures.product import products

quantity_updated = 256

@pytest.fixture()
def delivery_products(deliveries, products) -> list[DeliveryProduct]:
    return [
        DeliveryProduct.objects.create(
            id=1,
            quantity_delivered = 3,
            product = Product.objects.get(id=1),
            delivery = Delivery.objects.get(id=1)
        ),
        DeliveryProduct.objects.create(
            id=2,
            quantity_delivered = 4,
            product = Product.objects.get(id=2),
            delivery = Delivery.objects.get(id=2)
        )
    ]
    
# Payload to use in test.

# Create delivery_products
@pytest.fixture
def delivery_products_post_payload() -> dict:
    return {
        "quantity_delivered": 33,
        "product": 2,
        "delivery": 1
    }

# Create delivery_products wiht missing data
@pytest.fixture
def delivery_products_payload_missing_quantity() -> dict:
    return {    
        "product": 2,
        "delivery": 1
    }
    
# Update delivery_products
@pytest.fixture
def delivery_products_payload_update_quantity() -> dict:
    return {    
        "quantity_delivered": quantity_updated,
        "product": 1,
        "delivery": 2
    }
