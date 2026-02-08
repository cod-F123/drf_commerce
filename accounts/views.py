from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCorrectUser , IsOwner
from rest_framework.generics import CreateAPIView, UpdateAPIView , RetrieveUpdateDestroyAPIView , RetrieveAPIView , ListCreateAPIView
from .models import User , UserAddress
from .serializers import (RegisterUserSerializer , UpdateUsernameSerializer, 
                          ChangePasswordSerializer , UpdateUserInfoSerializer,
                          UserAddressSerializer, UserSerialzier)

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
    
    
class UserDetailApi(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsCorrectUser]
    serializer_class = UserSerialzier
    queryset = User.objects.all()
    lookup_field = "email"
    
    
class AddAndListUserAddressApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAddressSerializer
    
    def get_queryset(self):
        user_address_list = UserAddress.objects.filter(user__id = self.request.user.id)

        return user_address_list

class DetailAndUpdateAndDeleteUserAddressApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    lookup_field = "id"
    
