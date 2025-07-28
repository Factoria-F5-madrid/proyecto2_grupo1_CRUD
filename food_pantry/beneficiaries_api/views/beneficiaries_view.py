from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from beneficiaries_api.serializer import BeneficiaryRequestSerializer, BeneficiaryResponseSerializer
from beneficiaries_api.models import Beneficiary
from common.logger import Logger

class BeneficiariesView(Logger, APIView):
    @swagger_auto_schema(
        tags=['Beneficiaries'],
        operation_description="List all beneficiaries",
        responses={
            200: BeneficiaryResponseSerializer(many = True),
            400: "Bad Request"
        }
    )    
    def get(self, request: Request, *args, **kwargs) -> Response:
        """Gets all beneficiaries

        Args:
            request (Request): The request data

        Returns:
            Response: The response
        """
        self.debug(f"Getting all beneficiaries.")
        beneficiaries = Beneficiary.objects.all().values()
        response = BeneficiaryResponseSerializer(beneficiaries, many = True)
        return Response(response.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Beneficiaries'],
        operation_description="Creates a new beneficiary",
        request_body=BeneficiaryRequestSerializer,
        responses={
            201: "Beneficiary created",
            400: "Bad Request"
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Creates a benficiary

        Args:
            request (Request): The request data

        Returns:
            Response: The response
        """
        self.debug(f"Creating a beneficiary:  {request.data}.")
        data = BeneficiaryRequestSerializer(data=request.data)

        
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        
        self.debug(f"Data validation failed.")
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)