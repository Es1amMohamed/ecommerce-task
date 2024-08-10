from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status, viewsets
from django.contrib.auth import login


class UserAuthenticatedView(viewsets.ViewSet):

    @action(detail=False, methods=["post"])
    def register(self, request):
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
        data = request.data
        user_name = data.get("username")
        user = User.objects.filter(username=user_name).first()
        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
