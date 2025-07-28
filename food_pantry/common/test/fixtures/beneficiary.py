import pytest
from beneficiaries_api.models import Beneficiary

name_updated = "New beneficiary name" 

# Mock Beneficiary table with some records
@pytest.fixture()
def beneficiaries() -> list[Beneficiary]:
    return [
        Beneficiary.objects.create(
            id=1,
            name='Name 1',
            address='Address 1',
            contact_info='Contact Info 1'
        ),
        Beneficiary.objects.create(
            id=2,
            name='Name 2',
            address='Address 2',
            contact_info='Contact Info 2'
        )
    ]

# Payload to use in test.

# Create beneficiary
@pytest.fixture
def delivery_products_post_payload() -> dict:
    return {
        "name": "Beneficiary name",
        "Address": "Beneficiary address",
        "contact_info": "Beneficiary contact info",
    }

# Create beneficiary wiht missing data
@pytest.fixture
def beneficiary_payload_missing_name() -> dict:
    return {    
        "Address": "Beneficiary address",
        "contact_info": "Beneficiary contact info",
    }
    
# Update beneficary
@pytest.fixture
def beneficiary_payload_update_name() -> dict:
    return {    
        "name": name_updated
    }