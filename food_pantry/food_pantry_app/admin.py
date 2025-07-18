from django.contrib import admin


from donors_api.models import Donor
from categories_api.models import Category
from products_api.models import Product
from beneficiaries_api.models import Beneficiary
from deliveries_api.models import Delivery
from delivery_products_api.models import DeliveryProduct
from volunteers_api.models import Volunteer
from volunteer_deliveries_api.models import VolunteerDelivery   


# Register your models here.
admin.site.register(Donor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Beneficiary)
admin.site.register(Delivery)
admin.site.register(DeliveryProduct)
admin.site.register(Volunteer)
admin.site.register(VolunteerDelivery)









