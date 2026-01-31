from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCorrectUser
from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import User
from .serializers import RegisterUserSerializer , UpdateUsernameSerializer, ChangePasswordSerializer , UpdateUserInfoSerializer

# Create your views here.

class RegisterUserApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class UpdateUsernameApi(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsCorrectUser]
    queryset = User.objects.all()
    serializer_class = UpdateUsernameSerializer
    lookup_field = "email"
    

class ChangePasswordUserApi(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsCorrectUser]
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    lookup_field = "email"


class UpdateUserInfoApi(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsCorrectUser]
    queryset = User.objects.all()
    serializer_class = UpdateUserInfoSerializer
    lookup_field = "email"