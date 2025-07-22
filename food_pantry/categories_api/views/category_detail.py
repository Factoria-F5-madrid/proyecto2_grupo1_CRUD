# food_pantry/views/category_detail.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound # Para manejar objetos no encontrados
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models import Category # Importamos el modelo
from ..serializers import CategorySerializer # Importamos el serializador

class CategoryDetail(APIView):
    def get_object(self, pk):
        """
        Ayudante para obtener una categoría por su ID, o lanzar un error 404 si no existe.
        """
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound(detail="Categoría no encontrada.")

    @swagger_auto_schema(
        operation_description="Obtiene los detalles de una categoría específica por su ID.",
        responses={200: CategorySerializer(), 404: "Categoría no encontrada"}
    )
    def get(self, request, pk, format=None):
        """
        Obtiene los detalles de una categoría específica.
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Actualiza una categoría existente por su ID (todos los campos).",
        request_body=CategorySerializer,
        responses={200: CategorySerializer(), 400: "Datos inválidos", 404: "Categoría no encontrada"}
    )
    def put(self, request, pk, format=None):
        """
        Actualiza una categoría existente.
        """
        category = self.get_object(pk)
        # partial=True permitiría actualizar solo algunos campos, pero PUT espera todos los campos
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina una categoría existente por su ID.",
        responses={204: "No Content", 404: "Categoría no encontrada"}
    )
    def delete(self, request, pk, format=None):
        """
        Elimina una categoría específica.
        """
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)