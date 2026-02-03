from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwner
from .models import Order
from .serializers import OrderSerialzier

# Create your views here.

class CreateAndListOrderApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerialzier
    
    def get_queryset(self):
        return Order.objects.filter(user__id = self.request.user.id)
    
class DetailAndDeleteOrderApi(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = OrderSerialzier
    lookup_field = 'order_id'
    
    def get_queryset(self):
        return Order.objects.filter(user__id = self.request.user.id)