from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwner
from .models import Order
from .serializers import OrderSerializer

# Create your views here.

class CreateAndListOrderApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user__id = self.request.user.id)
    
class DetailAndDeleteOrderApi(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = OrderSerializer
    lookup_field = 'order_id'
    
    def get_queryset(self):
        return Order.objects.filter(user__id = self.request.user.id)