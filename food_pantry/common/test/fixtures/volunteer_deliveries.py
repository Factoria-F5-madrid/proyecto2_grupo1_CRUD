import pytest 
from volunteer_deliveries_api.models import VolunteerDelivery
from volunteers_api.models import Volunteer
from deliveries_api.models import Delivery
from common.test.fixtures.volunteer import volunteers
from common.test.fixtures.delivery import deliveries



delivery_updated = 1

# Mock Product table with some records
@pytest.fixture
def volunteer_deliveries(volunteers, deliveries) -> list[VolunteerDelivery]:
    return [
        VolunteerDelivery.objects.create(
            id=1,
            volunteer =  Volunteer.objects.get(id=1),
            delivery = Delivery.objects.get(id=1)
        ),
        VolunteerDelivery.objects.create(
            id=2,
            volunteer =  Volunteer.objects.get(id=2),
            delivery = Delivery.objects.get(id=2)
        )
    ]

# Payload to use in test.

# Create Volunteer Delivery
@pytest.fixture
def volunteer_delivery_post_payload() -> dict:
    return {
        "volunteer" : 2,
        "delivery": 2
    }

# Create volunteer_delivery wiht missing data
@pytest.fixture
def volunteer_delivery_payload_missing_delivery() -> dict:
    return {    
        "volunteer": 1,
    }
    
# Update volunteer_delivery
@pytest.fixture
def volunteer_delivery_payload_update_delivery() -> dict:
    return {    
        "delivery": delivery_updated,
        "volunteer": 1
    }
