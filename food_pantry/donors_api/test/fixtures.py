import pytest
from rest_framework.test import APIClient 
from donors_api.models import Donor

# Some common variables
name_updated = "My new name"

# Mock APIClient
@pytest.fixture()  
def api_client() -> APIClient:   # type: ignore
    """  
    Fixture to provide an API client  
    """  
    yield APIClient()
    
    
# Mock Donor table with some records
@pytest.fixture
def donors() -> list[Donor]:
    return [
        Donor.objects.create(
            id=1,
            name='Name 1',
            type='Type 1',
            contact='Contact 1',
            anonymous=False
        ),
        Donor.objects.create(
            id=2,
            name='Name 2',
            type='Type 2',
            contact='Contact 2',
            anonymous=False
        )
    ]


# Payload to use in test.

# Create donor
@pytest.fixture
def donor_post_payload() -> dict:
    return {
        "name": "Donor name",
        "type": "Donor type",
        "contact": "Donor contact",
        "anonymous": "True"
    }

# Create donor wiht missing data
@pytest.fixture
def donor_payload_missing_name() -> dict:
    return {    
        "type": "Donor type",
        "contact": "Donor contact",
        "anonymous": "True"
    }
    
# Update donor
@pytest.fixture
def donor_payload_update_name() -> dict:
    return {    
        "name": name_updated
    }
    
    