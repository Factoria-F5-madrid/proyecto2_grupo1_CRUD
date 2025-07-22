from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db import IntegrityError

from products_api.serializer import ProductRequestSerializer, ProductResponseSerializer
from products_api.models import Product
from common.logger import Logger

class ProductsView(Logger, APIView): 
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="List all products, or products filtered by donor_id and category_id",
        manual_parameters=[
            openapi.Parameter(
                'donor_id',
                openapi.IN_QUERY,
                description="Filter by donor ID.",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'category_id',
                openapi.IN_QUERY,
                description="Filter by category ID.",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            200: ProductResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        self.debug(f"Getting all products.")
        donor_id = request.query_params.get('donor_id')
        category_id = request.query_params.get('category_id')
        
        if category_id and donor_id:
            self.debug(f"Filtering by donor: {donor_id} and category: {category_id}.")
            products = Product.objects.filter(donor_id = donor_id, category_id=category_id).all().values()
        elif donor_id:
            self.debug(f"Filtering by donor: {donor_id}.")
            products = Product.objects.filter(donor_id = donor_id).all().values()
        elif category_id:
            self.debug(f"Filtering by category: {category_id}.")
            products = Product.objects.filter(category_id=category_id).all().values()
        else:
            self.debug(f"No filtering. Selecting all products.")
            products = Product.objects.all().values()   
            
        response = ProductResponseSerializer(products, many = True)
        
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="Creates a new product",
        request_body=ProductRequestSerializer,
        responses={
            201: "Product created",
            400: "Bad Request",
            500: "Internal server error"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        self.debug(f"Creating a product: {request.data}.")
        data = ProductRequestSerializer(data=request.data)
        
        if data.is_valid():
            try:
                data.save()
            except IntegrityError:
                self.error(f"Error creating product: {data.errors}")
                return Response(data.error_messages, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data.data, status=status.HTTP_201_CREATED)
        
        self.warning(f"Could not create a product: {data.errors}")
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)