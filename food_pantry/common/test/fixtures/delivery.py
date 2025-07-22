import pytest
from deliveries_api.models import Delivery
from beneficiaries_api.models import Beneficiary
from common.test.fixtures.beneficiary import beneficiaries

address_update = "New delivery address"

@pytest.fixture()
def deliveries(beneficiaries) -> list[Delivery]:
    return [
        Delivery.objects.create(
            id=1,
            delivery_date='2025-07-22',
            address='Address 1',
            beneficiary=Beneficiary.objects.get(id=1)
        ),
        Delivery.objects.create(
            id=2,
            delivery_date='2025-07-21',
            address='Address 2',
            beneficiary=Beneficiary.objects.get(id=2)
        )
    ]
    
# Payload to use in test.

# Create delivery
@pytest.fixture
def delivery_post_payload() -> dict:
    return {
        "delivery_date": "2025-07-20",
        "address": "Delivery address",
        "beneficiary": "2"
    }

# Create beneficiary wiht missing data
@pytest.fixture
def delivery_payload_missing_address() -> dict:
    return {    
        "delivery_date": "2025-07-20",
        "contact_info": "Beneficiary contact info",
        "beneficiary": "2"
    }
    
# Update beneficary
@pytest.fixture
def delivery_payload_update_address() -> dict:
    return {    
        "address": address_update,
        "beneficiary": 2
    }
