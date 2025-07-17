from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from donors_api.models import Donor
from donors_api.serializer import DonorResponse, DonorRequest


class DonorsView(APIView):
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="List all donors",
        responses={
            200: DonorResponse(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs):
        """_summary_

        Args:
            request (Request): _description_

        Returns:
            _type_: _description_
        """
        donors = Donor.objects.all().values()
        response = DonorResponse(donors, many = True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Creates a new donor",
        request_body=DonorRequest,
        responses={
            201: "Donor created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs):
        """_summary_

        Args:
            request (Request): _description_

        Returns:
            _type_: _description_
        """
        data = DonorRequest(data=request.data)
        
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)