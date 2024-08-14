from django.contrib import admin
from .models import OrderModel, OrderItemModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for OrderModel.

    This configuration sets up the admin interface for managing orders, including
    specifying which fields to display in the list view and which fields to filter by.

    List Display:
        - user: The user who placed the order.
        - total_price: The total price of the order.
        - created_at: The date and time when the order was created.

    List Filter:
        - user: Filter orders by the user who placed them.
        - created_at: Filter orders by their creation date.
    """

    list_display = ["user", "total_price", "created_at"]
    list_filter = ["user", "created_at"]


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for OrderItemModel.

    This configuration sets up the admin interface for managing order items, including
    specifying which fields to display in the list view and which fields to filter by.

    List Display:
        - order: The order to which the item belongs.
        - product: The product included in the order item.
        - quantity: The quantity of the product in the order item.

    List Filter:
        - order: Filter order items by the order they belong to.
    """

    list_display = ["order", "product", "quantity"]
    list_filter = ["order"]
