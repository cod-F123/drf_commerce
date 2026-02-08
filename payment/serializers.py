from rest_framework import serializers
from .models import Transaction
from orders.serializers import OrderSerializer

class TransactionSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    
    class Meta:
        model = Transaction
        fields = ["order","amount","ref_id","transaction_status","created_at"]