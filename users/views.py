from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from users import serializers
from users.models import User
# from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class UserView(APIView):
    def post(self, request):
        pass
