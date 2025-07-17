from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from donors_api.models import Donor
from donors_api.serializer import DonorResponseSerializer, DonorRequestSerializer


class DonorsView(APIView):
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="List all donors",
        responses={
            200: DonorResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all donors

        Args:
            request (Request): Request data

        Returns:
            Response: JSON will all donors
        """
        donors = Donor.objects.all().values()
        response = DonorResponseSerializer(donors, many = True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Creates a new donor",
        request_body=DonorRequestSerializer,
        responses={
            201: "Donor created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Creates a new donor

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with the response
        """
        data = DonorRequestSerializer(data=request.data)
        
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)