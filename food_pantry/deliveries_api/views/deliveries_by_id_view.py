from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from deliveries_api.models import Delivery
from deliveries_api.serializer import DeliveryRequestSerializer, DeliveryResponseSerializer 
from common.logger import Logger

class DeliveriesByIdView(Logger, APIView):
    def __get_object(self, id: int) -> Delivery:
        """Tries to get a delivery by its id. Returns none if not found.

        Args:
            id (int): Id of the delivery to retrieve

        Returns:
            Delivery: A delivery or None
        """
        self.debug(f"Getting a delivery from database with id: {id}")
        try:
            return Delivery.objects.get(id=id)
        except Delivery.DoesNotExist:
            self.warning(f"Delivery with id {id} not found in the database.")
            return None
        

    @swagger_auto_schema(
        tags=['Deliveries'],
        operation_description="List the delivery with id {id}",
        responses={
            200: DeliveryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )
    def get(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Gets a delivery by id and returns it

        Args:
            request (Request): Request data
            id (int): Id of delivery

        Returns:
            Response: JSON of delivery if found
        """
        self.debug(f"Getting delivery with id {id}.")
        delivery = self.__get_object(id)
        
        if not delivery:
            return Response({
                                "message": "Delivery with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = DeliveryResponseSerializer(delivery)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Deliveries'],
        operation_description="Updates the delivery with id {id} with the new values in the payload",
        request_body=DeliveryRequestSerializer,
        responses={
            200: DeliveryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )
    def put(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Updates a delivery by its id. Delivery must exist.

        Args:
            request (Request): Request data
            id (int): Id of the delivery to be updated

        Returns:
            Response: JSON of delivery updated
        """
        self.debug(f"Updating delivery with id {id}.")
        delivery = self.__get_object(id)
        if not delivery:
            return Response({
                                "message": "Delivery with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = DeliveryRequestSerializer(instance = delivery, data=request.data, partial = True )
        if data.is_valid():
            updated_delivery = data.save(commit=False)

            # If address is missing or empty, set it to the beneficiary's address
            if not updated_delivery.address:
                updated_delivery.address = updated_delivery.beneficiary.address

            updated_delivery.save()

            response_data = DeliveryResponseSerializer(updated_delivery)
            return Response(response_data.data, status=status.HTTP_200_OK)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    @swagger_auto_schema(
        tags=['Deliveries'],
        operation_description="Deletes the delivery with id {id}",
        responses={
            200: DeliveryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )
    def delete(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Deletes a delivery by its id

        Args:
            request (Request): Request data
            id (int): Id of delivery

        Returns:
            Response: JSON with the result of the operation
        """
        self.warning(f"Deleting delivery with id {id}.")
        delivery = self.__get_object(id)
        
        if not delivery:
            return Response({
                                "message": "Delivery with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        delivery.delete()        
        response = {
            "message": "Delivery with id " + str(id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)
    
    