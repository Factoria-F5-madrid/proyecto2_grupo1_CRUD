from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from delivery_products_api.serializer import DeliveryProductRequestSerializer, DeliveryProductResponseSerializer
from delivery_products_api.models import DeliveryProduct
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

# Configure logging
logger = logging.getLogger(__name__)

class DeliveryProductsView(APIView):
    """
    API view to list DeliveryProduct instances filtered by delivery date (GET)
    and to create new DeliveryProduct instances (POST).
    
    GET:
        - Query params:
            - date (str): Optional. Date in 'YYYY-MM-DD' format to filter deliveries.
            - confirm (str): Optional. If 'true', returns all records without filtering by date.
        - Returns a list of delivery products filtered by the given date,
            or all if confirmed, with a warning if no date provided.

    POST:
        - Expects a JSON payload to create a new DeliveryProduct.
    """
    @swagger_auto_schema(
        tags=['Delivery Products'],
        operation_description="List delivery products filtered by delivery date",
        manual_parameters=[
            openapi.Parameter('date', openapi.IN_QUERY, description="Filter by delivery date (YYYY-MM-DD)", type=openapi.TYPE_STRING),
            openapi.Parameter('confirm', openapi.IN_QUERY, description="Set to 'true' to retrieve all records without date filter", type=openapi.TYPE_STRING)
],
        responses={
            200: DeliveryProductResponseSerializer(many=True),
            400: "Bad Request: Invalid date format or missing confirmation",
        }
    )
    def get(self, request):
        """
        Retrieve delivery products filtered by delivery date.
        If no date provided, warns about large data and requires confirm param to proceed.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: List of serialized delivery products or warning message.
        """
        date_str = request.query_params.get('date')
        confirm = request.query_params.get('confirm', 'false').lower() == 'true'
        logger.info(f"GET request received with date='{date_str}' and confirm={confirm}")

        if date_str:
            try:
                delivery_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                delivery_products = DeliveryProduct.objects.filter(delivery__delivery_date=delivery_date)
                logger.info(f"Filtered delivery products by date: {delivery_date}, count={delivery_products.count()}")
            except ValueError:
                logger.error(f"Invalid date format received: {date_str}")
                return Response(
                    {"error": "Invalid date format. Use 'YYYY-MM-DD'."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        elif confirm:
            delivery_products = DeliveryProduct.objects.all()
            logger.info("No date provided, retrieving all delivery products as confirm is true.")
        else:
            logger.warning("No date provided and confirm not set to true. Returning warning.")
            return Response(
                {"warning": "No date provided. Use 'confirm=true' to retrieve all records."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = DeliveryProductResponseSerializer(delivery_products, many=True)
        logger.info(f"Returning {len(serializer.data)} delivery products.")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        tags=['Delivery Products'],
        operation_description="Create a new delivery product",
        request_body=DeliveryProductRequestSerializer,
        responses={
            201: DeliveryProductResponseSerializer,
            400: "Bad Request: Invalid data",
            500: "Internal Server Error"
        }
    )
    def post(self, request):
        
        """
        Create a new DeliveryProduct entry from the request data.

        Args:
            request (Request): The HTTP request object with JSON payload.

        Returns
            Response: Serialized created object or validation errors.
        """
        try:
            logger.info(f"Creating a new delivery product with data: {request.data}")
            serializer = DeliveryProductRequestSerializer(data=request.data)
            if serializer.is_valid():
                delivery_product = serializer.save()
                logger.info(f"Delivery product created successfully: ID {delivery_product.id}")
                response_serializer = DeliveryProductResponseSerializer(delivery_product)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            
            logger.warning(f"POST /delivery_products - Validation failed: {serializer.errors}")
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            logger.error("POST /delivery_products - Unexpected error occurred.", exc_info=True)
            return Response(
                {"error": "Failed to create delivery product.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            