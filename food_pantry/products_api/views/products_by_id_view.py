from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import IntegrityError

from products_api.serializer import ProductRequestSerializer, ProductResponseSerializer
from products_api.models import Product

class ProductsByIdView(APIView):
    def __get_object(self, id: int) -> Product:
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return None
        
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="List the product with id {id}",
        responses={
            200: ProductResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, id: int, *args, **kwargs) -> Response:
        product = self.__get_object(id)
        
        if not product:
            return Response({
                                "message": "Product with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = ProductResponseSerializer(product)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Updates the product with id {id} with the new values in the payload",
        request_body=ProductRequestSerializer,
        responses={
            200: ProductResponseSerializer(many = False),
            400: "Bad Request"
        }
    )  
    def put(self, request: Request, id: int, *args, **kwargs) -> Response:
        product = self.__get_object(id)
        if not product:
            return Response({
                                "message": "Product with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = ProductRequestSerializer(instance = product, data=request.data, partial = True )
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
            

    
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Deletes the product with id {id}",
        responses={
            200: ProductResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def delete(self, request: Request, id: int, *args, **kwargs) -> Response:
        product = self.__get_object(id)
        
        if not product:
            return Response({
                                "message": "Product with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        product.delete()        
        response = {
            "message": "Product with id " + str(id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)