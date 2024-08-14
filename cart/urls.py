from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet


app_name = "cart"


router = DefaultRouter()
router.register("cart", CartViewSet, basename="cart")

urlpatterns = [
    # Use a router to automatically generate routes for the registered viewsets
    path("", include(router.urls)),
    # Endpoint for adding an item to the user's cart
    # Method: POST
    # URL: /add/cart/<user_id>/
    path(
        "add/cart/<int:user_id>/",
        CartViewSet.as_view({"post": "add_to_cart"}),
        name="add_to_cart",
    ),
    # Endpoint for viewing the user's cart
    # Method: GET
    # URL: /cart/view/<user_id>/
    path(
        "cart/view/<int:user_id>/",
        CartViewSet.as_view({"get": "view_cart"}),
        name="view_cart",
    ),
    # Endpoint for removing an item from the user's cart
    # Method: DELETE
    # URL: /cart/remove/<user_id>/
    path(
        "cart/remove/<int:user_id>/",
        CartViewSet.as_view({"delete": "remove_from_cart"}),
        name="remove_from_cart",
    ),
]
