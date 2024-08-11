from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserAuthenticatedView

app_name = "users"


router = DefaultRouter()

router.register("users", UserAuthenticatedView, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserAuthenticatedView.as_view({"post": "register"})),
    ## URL for user registration.
    path("login/", UserAuthenticatedView.as_view({"post": "login"})),
    ## URL for user login.
]
