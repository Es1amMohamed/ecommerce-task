from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "orders"

urlpatterns = [
    # URL pattern to get items associated with a specific order
    # URL example: /orders/1/items
    # This route will call the 'order_items' method of the OrderViewSet to list all items for the given order.
    path(
        "orders/<int:pk>/items",
        views.OrderViewSet.as_view({"get": "list"}),
        name="order-list",
    ),
    # URL pattern to create a new order for a specific user
    # URL example: /orders/1
    # This route will call the 'create' method of the OrderViewSet to create a new order for the user with the given user_id.
    path(
        "orders/<int:user_id>",
        views.OrderViewSet.as_view({"post": "create"}),
        name="order-create",
    ),
]
