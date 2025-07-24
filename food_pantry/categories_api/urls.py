from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework.schemas.openapi import SchemaGenerator
from drf_yasg.views import get_schema_view as swagger_schema_view
from drf_yasg import openapi

base_url=""

schema_view = swagger_schema_view(
    openapi.Info(
        title="Food Pantry API",
        default_version='v1',
        description="API documentation for the Food Pantry project",
    ),
    public=True,
)
from .views import categories_view

base_url=""
    
urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs para la documentación de Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # <<-- AÑADE ESTA LÍNEA -->>
    path('food_pantry/v1/api/', include('food_pantry.urls')),
    path('admin/', admin.site.urls),
    path('food_pantry/v1/api/categories/', categories_view.CategoriesView.as_view()),
]