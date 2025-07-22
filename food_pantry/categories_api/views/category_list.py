# food_pantry/views/category_list.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models import Category # Importamos el modelo
from ..serializers import CategorySerializer # Importamos el serializador

# Definimos los parámetros de consulta para la documentación (opcional pero bueno)
category_list_get_params = [
    openapi.Parameter(
        'is_active',
        openapi.IN_QUERY,
        description="Filtrar por categorías activas (true/false)",
        type=openapi.TYPE_BOOLEAN,
        required=False
    )
]

class CategoryList(APIView):
    @swagger_auto_schema(
        operation_description="Obtiene todas las categorías o filtra por estado activo.",
        manual_parameters=category_list_get_params,
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request, format=None):
        """
        Lista todas las categorías.
        Puede filtrar por 'is_active'.
        """
        is_active = request.query_params.get('is_active', None)
        if is_active is not None:
            # Convertir 'true'/'false' a booleano
            is_active = is_active.lower() == 'true'
            categories = Category.objects.filter(is_active=is_active)
        else:
            categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Crea una nueva categoría.",
        request_body=CategorySerializer,
        responses={201: CategorySerializer(), 400: "Datos inválidos"}
    )
    def post(self, request, format=None):
        """
        Crea una nueva categoría.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)