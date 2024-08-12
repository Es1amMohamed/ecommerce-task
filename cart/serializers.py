from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "get_total_price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    get_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Cart
        fields = ["items", "get_total_price", "created_at"]
