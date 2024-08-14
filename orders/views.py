from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing orders.

    Provides CRUD operations for OrderModel and additional actions to list order items and create orders.
    Requires the user to be authenticated to perform any actions.

    Attributes:
        queryset (QuerySet): A QuerySet containing all order objects.
        serializer_class (OrderSerializer): The serializer class used for validating and serializing order data.
        permission_classes (list): A list of permission classes that the user must meet to access the ViewSet.

    Actions:
        order_items (GET): Retrieve items for a specific order.
        create (POST): Create a new order and return a success message.
    """

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["get"])
    def order_items(self, request, pk=None):
        """
        Retrieve items associated with a specific order.

        Args:
            request (Request): The HTTP request object.
            pk (int): The primary key of the order for which to retrieve items.

        Returns:
            Response: A Response object containing serialized order items data.
        """

        order = self.get_object()
        order_items = order.order_items.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def create(self, request, user_id, *args, **kwargs):
        """
        Create a new order and return a success message.

        This method overrides the default create method to add a custom success message to the response.

        Args:
            request (Request): The HTTP request object.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A Response object containing the serialized order data and a success message.
        """

        response = super().create(request, *args, **kwargs)
        response.data["message"] = "Order created successfully"
        return Response(response.data, status=status.HTTP_201_CREATED)
