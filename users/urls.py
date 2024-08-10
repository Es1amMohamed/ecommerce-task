from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserAuthenticatedView


router = DefaultRouter()

router.register("users", UserAuthenticatedView, basename="user")


app_name = "users"

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserAuthenticatedView.as_view({"post": "register"})),
    path("login/", UserAuthenticatedView.as_view({"post": "login"})),
]
