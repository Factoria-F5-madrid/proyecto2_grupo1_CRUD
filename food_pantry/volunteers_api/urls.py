# In here we place the URLs for the API (Swagger)
from django.urls import path

from .views.volunteers_view import VolunteersView
from .views.volunteer_by_id_view import VolunteerByIdView   

base_url = ""

urlpatterns = [
    path(base_url, VolunteersView.as_view(), name="volunteers"),
    path(base_url + '<int:volunteer_id>', VolunteerByIdView.as_view(), name="volunteer"),
]


    