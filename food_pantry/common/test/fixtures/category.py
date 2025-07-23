import pytest 
from categories_api.models import Category

name_updated = "New category name"

# Mock Category table with some records
@pytest.fixture
def categories() -> list[Category]:
    return [
        Category.objects.create(
            id=1,
            name='Name 1',
            description='Description 1'
        ),
        Category.objects.create(
            id=2,
            name='Name 2',
            description='Description 2'
        )
    ]


# # Payload to use in test.

# # Create donor
# @pytest.fixture
# def donor_post_payload() -> dict:
#     return {
#         "name": "Donor name",
#         "type": "Donor type",
#         "contact": "Donor contact",
#         "anonymous": "True"
#     }

# # Create donor wiht missing data
# @pytest.fixture
# def donor_payload_missing_name() -> dict:
#     return {    
#         "type": "Donor type",
#         "contact": "Donor contact",
#         "anonymous": "True"
#     }
    
# # Update donor
# @pytest.fixture
# def donor_payload_update_name() -> dict:
#     return {    
#         "name": name_updated
#     }
