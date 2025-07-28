import pytest 
from products_api.models import Product
from donors_api.models import Donor
from categories_api.models import Category
from common.test.fixtures.donor import donors
from common.test.fixtures.category import categories


name_updated = "New product name"

# Mock Product table with some records
@pytest.fixture
def products(donors, categories) -> list[Product]:
    return [
        Product.objects.create(
            id=1,
            name='Name 1',
            quantity=10,
            expiration_date='2026-11-30',
            donor= Donor.objects.get(id=1),
            category=Category.objects.get(id=2)
        ),
        Product.objects.create(
            id=2,
            name='Name 2',
            quantity=20,
            expiration_date='2026-12-30',
            donor= Donor.objects.get(id=2),
            category=Category.objects.get(id=2)
        )
    ]


# Payload to use in test.

# Create product
@pytest.fixture
def product_post_payload() -> dict:
    return {
        "name": "Product name",
        "quantity": 30,
        "expiration_date": "2027-12-12",
        "donor" : 1,
        "category": 2
    }

# Create product wiht missing data
@pytest.fixture
def product_payload_missing_name() -> dict:
    return {    
        "quantity": 30,
        "expiration_date": "2027-12-12",
        "donor" : 1,
        "category": 2
    }
    
# Update product
@pytest.fixture
def product_payload_update_name() -> dict:
    return {    
        "name": name_updated
    }
