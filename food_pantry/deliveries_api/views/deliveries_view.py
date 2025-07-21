from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from deliveries_api.models import Delivery
from deliveries_api.serializer import DeliveryRequestSerializer, DeliveryResponseSerializer
from common.logger import Logger

class DeliveriesView(Logger, APIView):
    @swagger_auto_schema(
        tags=['Deliveries'],
        operation_description="List all deliveries",
        responses={
            200: DeliveryResponseSerializer(many=True),
            400: "Bad Request"
        }
    )
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all deliveries

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with all deliveries
        """
        self.debug(f"Getting all deliveries.")
        deliveries = Delivery.objects.all()
        response = DeliveryResponseSerializer(deliveries, many=True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Deliveries'],
        operation_description="Creates a new delivery",
        request_body=DeliveryRequestSerializer,
        responses={
            201: "Delivery created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Creates a new delivery

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with the response
        """
        self.debug(f"Creating delivery: {request.data}.")
        data = DeliveryRequestSerializer(data=request.data)

        """If no address is provided, the beneficiary's address is used."""
        
        if data.is_valid():
            # Get the validated data
            validated_data = data.validated_data
            beneficiary = validated_data['beneficiary']
            address = validated_data.get('address')

            # If no address provided, use the beneficiary's address
            if not address:
                address = beneficiary.address

            # Create the delivery instance
            # Create the Delivery object manually to override address
            delivery = Delivery(
                delivery_date=validated_data['delivery_date'],
                beneficiary=beneficiary,
                address=address
            )

            # Save to the database
            delivery.save()

            
            response_data = DeliveryResponseSerializer(delivery)
            return Response(response_data.data, status=status.HTTP_201_CREATED)
        
        # If validation fails, return errors
        self.debug(f"Data validation failed.")
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
        


