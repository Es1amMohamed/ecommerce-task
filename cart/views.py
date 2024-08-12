from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import *


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)

    @action(detail=False, methods=["get"])
    def view_cart(self, request, user_id=None):
        """
        Retrieve the cart items for the current user.

        This action retrieves all items in the cart for the authenticated user.

        Response:
        - On success: Serialized cart items with HTTP 200 OK status.
        - If cart is not found: Empty list with HTTP 404 NOT FOUND status.
        """
        try:

            cart = Cart.objects.get(user=user_id)
            cart_items = CartItem.objects.filter(cart=cart)
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:

            return Response("Cart not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"])
    def add_to_cart(self, request, user_id=None):
        """
        Add a product to the cart of the specified user.

        This action adds a product to the cart for the user identified by user_id.
        If the cart for the user does not exist, it will raise a 404 error.

        Request Data:
        - product (str): The name of the product to add to the cart.
        - quantity (int, optional): The quantity of the product to add (default is 1).

        Response:
        - On success: Serialized data of the CartItem with HTTP 200 OK status.
        - If the cart or product does not exist: HTTP 404 Not Found.
        """

        cart = Cart.objects.get(user=user_id)
        data = request.data
        product = ProductModel.objects.get(name=data["product"])
        quantity = request.data.get("quantity", 1)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
