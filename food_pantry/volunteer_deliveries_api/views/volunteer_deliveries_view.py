from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from volunteer_deliveries_api.models import VolunteerDelivery
from volunteer_deliveries_api.serializer import VolunteerDeliveryRequestSerializer, VolunteerDeliveryResponseSerializer
from common.logger import Logger

class VolunteerDeliveriesView(Logger, APIView):
    @swagger_auto_schema(
        tags=['Volunteer Deliveries'],
        operation_description="List all volunteer deliveries",
        responses={
            200: VolunteerDeliveryResponseSerializer(many=True),
            400: "Bad Request"
        }
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all volunteer deliveries

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with all volunteer deliveries
        """
        self.debug("Getting all volunteer deliveries.")
        volunteer_deliveries = VolunteerDelivery.objects.all()
        response = VolunteerDeliveryResponseSerializer(volunteer_deliveries, many=True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Volunteer Deliveries'],
        operation_description="Creates a new volunteer delivery",
        request_body=VolunteerDeliveryRequestSerializer,
        responses={
            201: "Volunteer Delivery created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Creates a new volunteer delivery

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with the response
        """
        self.debug(f"Creating a new volunteer delivery: {request.data}.")
        data = VolunteerDeliveryRequestSerializer(data=request.data)

        if data.is_valid():
            data.save()
            return Response({"message": "Volunteer Delivery created successfully."}, status=status.HTTP_201_CREATED)
        
        self.debug("Data validation failed.")
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)