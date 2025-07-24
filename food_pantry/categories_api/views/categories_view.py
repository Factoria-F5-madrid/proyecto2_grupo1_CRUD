from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi # Importa openapi para definir parámetros manuales

# Asegúrate de que las importaciones del modelo y serializador sean correctas
# Basado en lo que definimos antes:
from categories_api.models import Category 
from categories_api.serializers import CategorySerializer 
# --- Parámetros de Swagger para el método GET de lista ---
# Define los parámetros manuales aquí, para ser usados en el decorador @swagger_auto_schema
category_list_get_params = [
    openapi.Parameter(
        'is_active', # Nombre del parámetro de la query
        openapi.IN_QUERY, # Indica que es un parámetro de la URL (query parameter)
        description="Filtrar por categorías activas (true/false).",
        type=openapi.TYPE_BOOLEAN, # Tipo de dato esperado
        required=False # Es opcional
    )
]

class CategoryListCreateView(APIView):
    """
    Vista para listar todas las categorías o crear una nueva.
    Permite filtrar por el estado 'is_active'.
    """

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Lista todas las categorías, opcionalmente filtradas por estado activo.",
        # Aquí usamos manual_parameters para el filtro 'is_active'
        manual_parameters=category_list_get_params,
        responses={
            200: CategorySerializer(many=True), # Respuesta para la lista
            400: "Solicitud inválida"
        }
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Obtiene todas las categorías o filtra por estado activo.
        """
        is_active = request.query_params.get('is_active', None)

        if is_active is not None:
            # Convertir 'true'/'false' a booleano de forma segura
            is_active_bool = is_active.lower() == 'true'
            # Asumiendo que tu modelo Category tiene un campo 'is_active'
            # Si no lo tiene, deberías añadirlo o eliminar esta lógica de filtro
            categories = Category.objects.filter(is_active=is_active_bool)
        else:
            categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Crea una nueva categoría.",
        # Usa el serializador directamente para la estructura del cuerpo de la solicitud
        request_body=CategorySerializer,
        responses={
            201: CategorySerializer(), # Respuesta para la categoría creada
            400: "Datos inválidos"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Crea una nueva categoría.
        """
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # Devolvemos los datos serializados de la categoría creada, incluyendo el ID
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    """
    Vista para recuperar, actualizar o eliminar una categoría específica por su ID.
    """

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Obtiene los detalles de una categoría específica por ID.",
        responses={
            200: CategorySerializer(),
            404: "Categoría no encontrada"
        }
    )
    def get(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """
        Obtiene los detalles de una categoría específica.
        """
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"detail": "Categoría no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Actualiza una categoría existente por ID.",
        request_body=CategorySerializer,
        responses={
            200: CategorySerializer(),
            400: "Datos inválidos",
            404: "Categoría no encontrada"
        }
    )
    def put(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """
        Actualiza una categoría existente.
        """
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"detail": "Categoría no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=False) # partial=False para PUT (actualización completa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Actualiza parcialmente una categoría existente por ID.",
        request_body=CategorySerializer, # Puede ser el mismo serializador, DRF manejará los campos parciales
        responses={
            200: CategorySerializer(),
            400: "Datos inválidos",
            404: "Categoría no encontrada"
        }
    )
    def patch(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """
        Actualiza parcialmente una categoría existente.
        """
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"detail": "Categoría no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True) # partial=True para PATCH (actualización parcial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Elimina una categoría por ID.",
        responses={
            204: "Categoría eliminada",
            404: "Categoría no encontrada"
        }
    )
    def delete(self, request: Request, pk: int, *args, **kwargs) -> Response:
        """
        Elimina una categoría existente.
        """
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"detail": "Categoría no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)