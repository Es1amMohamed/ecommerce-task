from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet


app_name = "cart"


router = DefaultRouter()
router.register("cart", CartViewSet, basename="cart")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "add/cart/<int:user_id>/",
        CartViewSet.as_view({"post": "add_to_cart"}),
        name="add_to_cart",
    ),
    path(
        "cart/view/<int:user_id>/",
        CartViewSet.as_view({"get": "view_cart"}),
        name="view_cart",
    ),
    path(
        "cart/remove/<int:user_id>/",
        CartViewSet.as_view({"delete": "remove_from_cart"}),
        name="remove_from_cart",
    ),
]
