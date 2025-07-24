import pytest 
from donors_api.models import Donor

name_updated = "New donor name"

# Mock Donor table with some records
@pytest.fixture
def donors() -> list[Donor]:
    return [
        Donor.objects.create(
            id=1,
            name='Name 1',
            type='individual',
            contact='Contact 1',
            anonymous=False
        ),
        Donor.objects.create(
            id=2,
            name='Name 2',
            type='institución',
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
        "type": Donor.DONOR_TYPES[0][0], # "individual"
        "contact": "Donor contact",
        "anonymous": True
    }

# Create donor wiht missing data
@pytest.fixture
def donor_payload_missing_name() -> dict:
    return {    
        "type": Donor.DONOR_TYPES[1][1], # "institución"
        "contact": "Donor contact",
        "anonymous": True
    }
    
# Update donor
@pytest.fixture
def donor_payload_update_name() -> dict:
    return {    
        "name": name_updated
    }