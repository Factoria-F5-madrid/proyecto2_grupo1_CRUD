from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from products_api.serializer import ProductRequestSerializer, ProductResponseSerializer
from products_api.models import Product

class ProductsView(APIView):
    def __valid_params(self, donor_id, category_id):
        if not donor_id and category_id:
            return False
        if donor_id and not category_id:
            return False
        return True
    
    @swagger_auto_schema(
        tags=['Products'],
        operation_description="List all products, or products filtered by donor_id and category_id",
        manual_parameters=[
            openapi.Parameter(
                'donor_id',
                openapi.IN_QUERY,
                description="Donor ID. If present, Category ID must be present",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'category_id',
                openapi.IN_QUERY,
                description="Category ID. If present, Donor ID must be present.",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={
            200: ProductResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        donor_id = request.query_params.get('donor_id')
        category_id = request.query_params.get('category_id')
        if not self.__valid_params(donor_id, category_id):
            return Response("donor_id or category_id is missing", status.HTTP_400_BAD_REQUEST)
        
        #TODO Filter by parameters if true
        
        products = Product.objects.all().values()
        response = ProductResponseSerializer(products, many = True)
        
        return Response(response.data, status=status.HTTP_200_OK)