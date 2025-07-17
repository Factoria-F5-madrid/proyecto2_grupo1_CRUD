from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from donors_api.models import Donor
from donors_api.serializer import DonorResponse, DonorRequest


class DonorsByDonorIdView(APIView):
    def __get_object(self, todo_id):
        """_summary_

        Args:
            todo_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            return Donor.objects.get(id=todo_id)
        except Donor.DoesNotExist:
            return None
        
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="List the donor with id {donor_id}",
        responses={
            200: DonorResponse(many = False),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, donor_id, *args, **kwargs):
        """_summary_

        Args:
            request (Request): _description_
            donor_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        donor = self.__get_object(donor_id)
        
        if not donor:
            return Response({
                                "message": "Donor with id " + str(donor_id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = DonorResponse(donor)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Updates the donor with id {donor_id} with the new values in the payload",
        request_body=DonorRequest,
        responses={
            200: DonorResponse(many = False),
            400: "Bad Request"
        }
    )  
    def put(self, request: Request, donor_id, *args, **kwargs):
        """_summary_

        Args:
            request (Request): _description_
            donor_id (_type_): _description_
            payload (DonorRequest): _description_

        Returns:
            _type_: _description_
        """
        
        donor = self.__get_object(donor_id)
        if not donor:
            return Response({
                                "message": "Donor with id " + str(donor_id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = DonorRequest(instance = donor, data=request.data, partial = True )
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
            

    
    @swagger_auto_schema(
        tags=['Donors'],
        operation_description="Deletes the donor with id {donor_id}",
        responses={
            200: DonorResponse(many = False),
            400: "Bad Request"
        }
    )    
    def delete(self, request: Request, donor_id, *args, **kwargs):
        """_summary_

        Args:
            request (Request): _description_
            donor_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        donor = self.__get_object(donor_id)
        
        if not donor:
            return Response({
                                "message": "Donor with id " + str(donor_id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        donor.delete()        
        response = {
            "message": "Donor with id " + str(donor_id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)