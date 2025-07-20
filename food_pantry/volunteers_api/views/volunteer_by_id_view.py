from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from volunteers_api.models import Volunteer
from volunteers_api.serializer import VolunteerResponseSerializer, VolunteerRequestSerializer


class VolunteerByIdView(APIView):
    def __get_object(self, id: int) -> Volunteer:
        """Tries to get a volunteer by its id. Returns none if not found.

        Args:
            id (int): Id of the volunteer to retrieve

        Returns:
            Volunteer: A volunteer or None
        """
        try:
            return Volunteer.objects.get(id=id)
        except Volunteer.DoesNotExist:
            # If the volunteer does not exist, return None
            return None
        except Exception as e:
            # If any other exception occurs, log it and return None
            print(f"An error occurred while retrieving the volunteer: {e}")
            return None
        
    @swagger_auto_schema(
        tags=['Volunteers'],
        operation_description="List the volunteer with id {id}",
        responses={
            200: VolunteerResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Gets a volunteer by id and returns it

        Args:
            request (Request): Request data
            id (int): Id of volunteer

        Returns:
            Response: JSON of volunteer if found
        """
        
        volunteer = self.__get_object(id)
        
        if not volunteer:
            return Response({
                                "message": "Volunteer with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = VolunteerResponseSerializer(volunteer)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Volunteers'],
        operation_description="Updates the volunteer with id {id} with the new values in the payload",
        request_body=VolunteerRequestSerializer,
        responses={
            200: VolunteerResponseSerializer(many = False),
            400: "Bad Request"
        }
    )  
    def put(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Updates a volunteer by its id. Volunteer must exist.

        Args:
            request (Request): Request data
            id (int): Id of the volunteer to be updated

        Returns:
            Response: JSON of volunteer updated
        """
        
        volunteer = self.__get_object(id)
        if not volunteer:
            return Response({
                                "message": "Volunteer with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = VolunteerRequestSerializer(instance = volunteer, data=request.data, partial = True )
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
            

    
    @swagger_auto_schema(
        tags=['Volunteers'],
        operation_description="Deletes the volunteer with id {id}",
        responses={
            200: VolunteerResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def delete(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Delete a volunteer by their id

        Args:
            request (Request): Request data
            id (int): Id of the volunteer to be deleted

        Returns:
            Response: JSON with the result of the operation
        """
        
        volunteer = self.__get_object(id)
        
        if not volunteer:
            return Response({
                                "message": "Volunteer with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        volunteer.delete()        
        response = {
            "message": "Volunteer with id " + str(id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)