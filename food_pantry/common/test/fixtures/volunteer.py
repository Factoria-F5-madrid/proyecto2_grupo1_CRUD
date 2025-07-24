import pytest 
from volunteers_api.models import Volunteer

name_updated = "New volunteer name"

# Mock Donor table with some records
@pytest.fixture
def volunteers() -> list[Volunteer]:
    return [
        Volunteer.objects.create(
            id=1,
            name='Name 1',
            email='Email 1'
        ),
        Volunteer.objects.create(
            id=2,
            name='Name 2',
            email='Email 2',
        )
    ]


# Payload to use in test.

# Create volunteer
@pytest.fixture
def volunteer_post_payload() -> dict:
    return {
        "name": "Volunteer name",
        "email": "email@my.email.com"
    }

# Create volunteer wiht missing data
@pytest.fixture
def volunteer_payload_missing_name() -> dict:
    return {    
        "email": "email@my.email.com"
    }
    
# Update volunteer
@pytest.fixture
def volunteer_payload_update_name() -> dict:
    return {    
        "name": name_updated
    }