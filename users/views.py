from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status, viewsets
from django.contrib.auth import login


class UserAuthenticatedView(viewsets.ViewSet):
    """
    A ViewSet for managing user authentication including registration and login.
    """

    @action(detail=False, methods=["post"])
    def register(self, request):
        """
        Register a new user.

            This action creates a new user based on the provided username and other details.
            If the user already exists, a message indicating this will be returned.

            Request Data:
            - username: The username for the new user.
            - Other user details as required by the UserSerializer.

            Response:
            - On successful registration: Serialized user data with HTTP 201 Created status.
            - If the username already exists: Error message with HTTP 400 Bad Request status.
            - If the provided data is invalid: Error details with HTTP 400 Bad Request status.
        """
        data = request.data
        user_name = data.get("username")
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            if not User.objects.filter(username=user_name).exists():
                serializer.save()
                login(request, serializer.instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(
                {"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"])
    def login(self, request):
        """
        Authenticate a user and log them in.

        This action logs in a user based on the provided username. If the user is found,
        they will be logged in, and their data will be returned.

        Request Data:
        - username: The username of the user attempting to log in.

        Response:
        - On successful login: Serialized user data with HTTP 200 OK status.
        - If the user is not found: Error message with HTTP 404 Not Found status.
        """

        data = request.data
        user_name = data.get("username")
        user = User.objects.filter(username=user_name).first()
        if user:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            serializer = UserSerializer(user)
            return Response(
                {
                    "user": serializer.data,
                    "access": access_token,
                    "refresh": str(refresh),
                },
                status=status.HTTP_200_OK,
            )
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
