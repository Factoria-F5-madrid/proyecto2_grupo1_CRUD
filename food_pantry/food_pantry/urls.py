"""
URL configuration for food_pantry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .swagger import CustomOpenAPISchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Food Pantry API",
        default_version='v1',
        description="A list of public APIs available for the Food Pantry application.",
        #terms_of_service="https://www.example.com/terms/",
        #contact=openapi.Contact(email="contact@example.com"),
        #license=openapi.License(name="Awesome License"),
    ),
    generator_class=CustomOpenAPISchemaGenerator,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_pantry/', include('food_pantry_app.urls')),              # Home page entry point
    path('food_pantry/api/v1/', include(
        [
            path('beneficiaries/', include('beneficiaries_api.urls')),
            path('donors/', include('donors_api.urls')),
            path('products/', include('products_api.urls')),
            path('volunteers/', include('volunteers_api.urls')),
            path('doc/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
        ]
    ))
]