from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from beneficiaries_api.models import Beneficiary
from beneficiaries_api.serializer import BeneficiaryRequestSerializer, BeneficiaryResponseSerializer


class BeneficiariesByIdView(APIView):
    def __get_object(self, id: int) -> Beneficiary:
        """Gets an object from the database or none

        Args:
            id (int): Id to retrieve

        Returns:
            Beneficiary: A record
        """
        try:
            return Beneficiary.objects.get(id=id)
        except Beneficiary.DoesNotExist:
            return None
        
    @swagger_auto_schema(
        tags=['Beneficiaries'],
        operation_description="List the beneficiary with id {id}",
        responses={
            200: BeneficiaryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, id: int, *args, **kwargs) -> Response:   
        """Gets a record from the database

        Args:
            request (Request): The request data
            id (int): Id to retrieve

        Returns:
            Response: The response
        """
        beneficiary = self.__get_object(id)
        
        if not beneficiary:
            return Response({
                                "message": "Beneficiary with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        response = BeneficiaryResponseSerializer(beneficiary)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Beneficiaries'],
        operation_description="Updates the beneficiary with id {id} with the new values in the payload",
        request_body=BeneficiaryRequestSerializer,
        responses={
            200: BeneficiaryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )  
    def put(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Updates a record from the database

        Args:
            request (Request): The request data
            id (int): Id to retrieve

        Returns:
            Response: The response
        """
        beneficiary = self.__get_object(id)
        if not beneficiary:
            return Response({
                                "message": "Beneficiary with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
            
        data = BeneficiaryRequestSerializer(instance = beneficiary, data=request.data, partial = True )
        if data.is_valid():
            data.save()
        return Response(data.data, status=status.HTTP_200_OK)
            

    
    @swagger_auto_schema(
        tags=['Beneficiaries'],
        operation_description="Deletes the beneficiary with id {id}",
        responses={
            200: BeneficiaryResponseSerializer(many = False),
            400: "Bad Request"
        }
    )    
    def delete(self, request: Request, id: int, *args, **kwargs) -> Response:
        """Deletes a record from the database

        Args:
            request (Request): The request data
            id (int): Id to retrieve

        Returns:
            Response: The response
        """
        beneficiary = self.__get_object(id)
        
        if not beneficiary:
            return Response({
                                "message": "Beneficiary with id " + str(id) + " does not exists."
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                            )
    
        beneficiary.delete()        
        response = {
            "message": "Beneficiary with id " + str(id) + " has been removed."
        }
    
        return Response(response, status=status.HTTP_200_OK)