from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from volunteer_deliveries_api.models import VolunteerDelivery
from volunteer_deliveries_api.serializer import VolunteerDeliveryRequestSerializer, VolunteerDeliveryResponseSerializer 

class VolunteerDeliveriesByIdView(APIView):
    def __get_object(self, delivery_id: int) -> VolunteerDelivery:
        """Tries to get a volunteer delivery by its delivery id. Returns none if not found.

        Args:
            delivery_id (int): Id of the delivery to retrieve

        Returns:
            VolunteerDelivery: A volunteer delivery or None
        """
        try:
            return VolunteerDelivery.objects.get(delivery_id=delivery_id)
        except VolunteerDelivery.DoesNotExist:
            return None

    @swagger_auto_schema(
        tags=['Volunteer Deliveries'],
        operation_description="List the volunteer delivery with id {delivery_id}",
        responses={
            200: VolunteerDeliveryResponseSerializer(many=False),
            400: "Bad Request"
        }
    )
    def get(self, request: Request, delivery_id: int, *args, **kwargs) -> Response:
        """Gets a volunteer delivery by delivery id and returns it

        Args:
            request (Request): Request data
            delivery_id (int): Id of the delivery

        Returns:
            Response: JSON of volunteer delivery if found
        """
        
        volunteer_delivery = self.__get_object(delivery_id)
        
        if not volunteer_delivery:
            return Response({
                                "message": "Volunteer Delivery with id " + str(delivery_id) + " does not exist."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = VolunteerDeliveryResponseSerializer(volunteer_delivery)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Volunteer Deliveries'],
        operation_description="Updates the volunteer delivery with id {delivery_id} with the new values in the payload",
        request_body=VolunteerDeliveryRequestSerializer,
        responses={
            200: VolunteerDeliveryResponseSerializer(many=False),
            400: "Bad Request"
        }
    )
    def put(self, request: Request, delivery_id: int, *args, **kwargs) -> Response:
        """Updates a volunteer delivery by delivery id

        Args:
            request (Request): Request data
            delivery_id (int): Id of the delivery

        Returns:
            Response: JSON of updated volunteer delivery if successful
        """
        
        volunteer_delivery = self.__get_object(delivery_id)
        if not volunteer_delivery:
            return Response({
                                "message": "Volunteer Delivery with id " + str(delivery_id) + " does not exist."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST) 
        
        data = VolunteerDeliveryRequestSerializer(isinstance = volunteer_delivery, data=request.data, partial=True) 
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Volunteer Deliveries'],
        operation_description="Deletes the volunteer delivery with id {delivery_id}",
        responses={
            204: "Volunteer Delivery deleted",
            400: "Bad Request"
        }
    )
    def delete(self, request: Request, delivery_id: int, *args, **kwargs) -> Response:
        """Deletes a volunteer delivery by its id

        Args:
            request (Request): Request data
            delivery_id (int): Id of the delivery to be deleted

        Returns:
            Response: JSON of success message if deleted, or error if not found
        """
        
        volunteer_delivery = self.__get_object(delivery_id)
        if not volunteer_delivery:
            return Response({
                                "message": "Volunteer Delivery with id " + str(delivery_id) + " does not exist."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        volunteer_delivery.delete()
        response = {
            "message": "Volunteer Delivery with id " + str(delivery_id) + " deleted successfully."  
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)



    