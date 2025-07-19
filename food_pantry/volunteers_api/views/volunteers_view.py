from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from volunteers_api.models import Volunteer
from volunteers_api.serializer import VolunteerResponseSerializer, VolunteerRequestSerializer



class VolunteersView(APIView):
    @swagger_auto_schema(
        tags=['Volunteers'],
        operation_description="List all volunteers",
        responses={
            200: VolunteerResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all volunteers

        Args:
            request (Request): Request data

        Returns:
            Response: JSON will all volunteers
        """
        volunteers = Volunteer.objects.all().values()
        response = VolunteerResponseSerializer(volunteers, many = True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Volunteers'],
        operation_description="Create a new volunteer",
        request_body=VolunteerRequestSerializer,
        responses={
            201: "Volunteer created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Create a new volunteer

        Args:
            request (Request): Request data

        Returns:
            Response: JSON with the response
        """
        data = VolunteerRequestSerializer(data=request.data)
        
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)