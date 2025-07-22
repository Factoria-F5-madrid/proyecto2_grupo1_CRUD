from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from donors_api.models import Categories
from donors_api.serializer import CategoriesResponseSerializer, CategoriesRequestSerializer


class CategoriesView(APIView):
    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="List all categories",
        responses={
            200: CategoriesResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all categories

        Args:
            request (Request): Request data

        Returns:
            Response: JSON will all donors
        """
        categories = Categories.objects.all().values()
        response = CategoriesResponseSerializer(categories, many = True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Categories'],
        operation_description="Creates a new category",
        request_body=CategoriesRequestSerializer,
        responses={
            201: "Category created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Creates a new category

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with the response
        """
        data = CategoriesRequestSerializer(data=request.data)
        
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)