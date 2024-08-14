from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the CartItem model.

    This serializer is used to represent individual items in a shopping cart.
    It includes the product name and quantity of each item, and calculates the total price
    for the item based on its quantity and unit price.

    Fields:
        product (str): The name of the product, represented as a string using the __str__ method of the Product model.
        quantity (int): The number of units of the product in the cart.
        get_total_price (float): The total price for the cart item, calculated as quantity multiplied by the product's unit price.
    """

    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "get_total_price"]


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cart model.

    This serializer is used to represent a shopping cart and its contents.
    It includes all items currently in the cart and the total price of the cart.

    Fields:
        items (list): A list of CartItem objects representing the items in the cart.
        get_total_price (float): The total price for all items in the cart, calculated as the sum of the total prices of each item.
        created_at (datetime): The date and time when the cart was created.
    """

    items = CartItemSerializer(many=True, read_only=True)
    get_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ["items", "get_total_price", "created_at"]
