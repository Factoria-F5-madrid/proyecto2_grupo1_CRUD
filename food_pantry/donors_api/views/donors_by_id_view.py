from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from donors_api.models import Donor
from donors_api.serializer import DonorResponseSerializer, DonorRequestSerializer


class DonorsByIdView(APIView):
    def __get_object(self, id) -> Donor:
        """Tries to get a donor by its id. Returns none if not found.

        Args:
            id (int): Id of the donor to retrieve

        Returns:
            Donor: A donor or None
        """
        try:
            return Donor.objects.get(id=id)
        except Donor.DoesNotExist:
            return None
        
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="List the donor with id {id}",
        responses={
            200: DonorResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Gets a donor by id and returns it

        Args:
            request (Request): Request data
            id (int): Id of donor

        Returns:
            Response: JSON of donor if found
        """
        
        donor = self.__get_object(id)
        
        if not donor:
            return Response({
                                "message": "Donor with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = DonorResponseSerializer(donor)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Updates the donor with id {id} with the new values in the payload",
        request_body=DonorRequestSerializer,
        responses={
            200: DonorResponseSerializer(many = False),
            400: "Bad Request"
        }
    )  
    def put(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Updates a donor by its id. Donor must exist.

        Args:
            request (Request): Request data
            id (int): Id of the donor to be updated

        Returns:
            Response: JSON of donor updated
        """
        
        donor = self.__get_object(id)
        if not donor:
            return Response({
                                "message": "Donor with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = DonorRequestSerializer(instance = donor, data=request.data, partial = True )
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
            

    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Deletes the donor with id {id}",
        responses={
            200: DonorResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def delete(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Deletes a donor by its id

        Args:
            request (Request): Request data
            id (int): Id of donor

        Returns:
            Response: JSON with the result of the operation
        """
        
        donor = self.__get_object(id)
        
        if not donor:
            return Response({
                                "message": "Donor with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        donor.delete()        
        response = {
            "message": "Donor with id " + str(id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)