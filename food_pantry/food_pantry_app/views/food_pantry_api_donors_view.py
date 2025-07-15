from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FoodPantryApiDonorsView(APIView):
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="List all donors",
        responses={
            200: "Donors listed"
        }
    )    
    def get(self, request: Request):
        return Response([])
    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Creates a new donor",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "address": openapi.Schema(type=openapi.TYPE_STRING)
            },
            description="The data to be entered in the body"
        ),
        responses={
            201: "Donor created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request):
        return Response("Push donors")