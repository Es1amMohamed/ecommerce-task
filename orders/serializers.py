from rest_framework import serializers
from .models import OrderModel, OrderItemModel
from cart.models import Cart


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderItemModel.

    This serializer handles the representation of order items, including the product and quantity.

    Attributes:
        product (str): A human-readable representation of the product.
        quantity (int): The quantity of the product in the order item.
    """

    class Meta:
        model = OrderItemModel
        fields = ["product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for OrderModel.

    This serializer handles the representation of orders, including associated products, address details, and order statuses.
    It also manages the creation of orders by transferring products from the user's cart.
    """

    products = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = [
            "products",
            "country",
            "city",
            "state",
            "street",
            "phone",
            "zip_code",
            "order_status",
            "payment_status",
            "payment_method",
            "total_price",
            "created_at",
        ]
        read_only_fields = ["products", "created_at", "total_price"]

    def create(self, validated_data):
        """
        Create a new order based on the current user's cart.

        This method creates an order and populates it with items from the user's cart. It also calculates the total price of the order
        and clears the cart items once the order is successfully created.

        Args:
            validated_data (dict): The validated data for the order.

        Returns:
            OrderModel: The created order instance.

        Raises:
            serializers.ValidationError: If the user does not have an active cart or if there are no products in the cart.
        """

        user = self.context["request"].user
        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("The user does not have an active cart.")

        cart_items = cart.items.all()
        if not cart_items.exists():
            raise serializers.ValidationError("No products in the cart.")

        order = OrderModel.objects.create(user=user, **validated_data)

        total_price = 0
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            OrderItemModel.objects.create(
                order=order, product=product, quantity=quantity
            )
            total_price += product.price * quantity

        order.total_price = total_price
        order.save()
        cart.items.all().delete()

        return order
