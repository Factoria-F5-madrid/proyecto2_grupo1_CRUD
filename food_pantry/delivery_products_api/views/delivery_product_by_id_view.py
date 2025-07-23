from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema

from delivery_products_api.models import DeliveryProduct
from delivery_products_api.serializer import (
    DeliveryProductRequestSerializer,
    DeliveryProductResponseSerializer
)
from common.logger import Logger

class DeliveryProductByIdView(Logger, APIView):
    """
    API View for retrieving, updating, and deleting a DeliveryProduct by ID.
    Does not crash on errors — returns meaningful messages and logs them.
    """
    @swagger_auto_schema(
        tags=['Delivery Products'],
        operation_description="Retrieve, update, or delete a delivery product by ID",
        responses={
            200: DeliveryProductResponseSerializer,
            404: "Not Found: Delivery product with the given ID does not exist.",
            400: "Bad Request: Invalid data provided for update.",
            500: "Internal Server Error: Unexpected error occurred."
        }
    )
    def get(self, request, id):
        """
        Retrieve a delivery product by its ID.
        """
        try:
            delivery_product = get_object_or_404(DeliveryProduct, id=id)
            serializer = DeliveryProductResponseSerializer(delivery_product)
            self.info(f"Retrieved DeliveryProduct with ID {id}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            self.warning(f"DeliveryProduct with ID {id} not found")
            return Response({"error": "Delivery product not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            self.error(f"Unexpected error in GET DeliveryProduct ID {id}: {e}")
            return Response({"error": "Server error retrieving product."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(
        tags=['Delivery Products'],
        operation_description="Update a delivery product by ID",
        request_body=DeliveryProductRequestSerializer,
        responses={
            200: DeliveryProductResponseSerializer,
            404: "Not Found: Delivery product with the given ID does not exist.",
            400: "Bad Request: Invalid data provided for update.",
            500: "Internal Server Error: Unexpected error occurred."
        }
    )
    def put(self, request, id):
        """
        Update a delivery product by its ID.
        """
        try:
            delivery_product = get_object_or_404(DeliveryProduct, id=id)
            serializer = DeliveryProductRequestSerializer(delivery_product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                self.info(f"Updated DeliveryProduct with ID {id}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            self.warning(f"Validation failed for PUT DeliveryProduct ID {id}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            self.warning(f"Cannot update — DeliveryProduct with ID {id} not found")
            return Response({"error": "Delivery product not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            self.error(f"Unexpected error in PUT DeliveryProduct ID {id}: {e}")
            return Response({"error": "Server error updating product."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(
        tags=['Delivery Products'],
        operation_description="Delete a delivery product by ID",
        responses={
            204: "No Content: Delivery product deleted successfully.",
            404: "Not Found: Delivery product with the given ID does not exist.",
            500: "Internal Server Error: Unexpected error occurred."
        }
    )
    def delete(self, request, id):
        """
        Delete a delivery product by its ID.
        """
        try:
            delivery_product = get_object_or_404(DeliveryProduct, id=id)
            delivery_product.delete()
            self.info(f"Deleted DeliveryProduct with ID {id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            self.warning(f"Cannot delete — DeliveryProduct with ID {id} not found")
            return Response({"error": "Delivery product not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            self.error(f"Unexpected error in DELETE DeliveryProduct ID {id}: {e}")
            return Response({"error": "Server error deleting product."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
