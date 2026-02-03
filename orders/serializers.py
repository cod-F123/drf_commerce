from rest_framework import serializers
from django.db import transaction
from decimal import Decimal
from .utils import get_order_settings
from .models import Order , OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(read_only=True, max_digits=12, decimal_places=2)
    
    class Meta:
        model = OrderItem
        fields = ['product','amount','quantity']
        
    def validate(self, attrs):
        max_qty = get_order_settings('MAXIMUM_PRODUCT_QUANTITY',3)
        
        if attrs['quantity'] > max_qty:
            raise serializers.ValidationError(
                'Maximum quantity per product exceeded.'
            )
            
        product = attrs['product']
        
        # check stok
        if product.stock < attrs['quantity'] :
            raise serializers.ValidationError(
                    f'Not enough stock for {product.name}'
                )
            
        
        
        return super().validate(attrs)
    

class OrderSerialzier(serializers.ModelSerializer):
    
    items = OrderItemSerializer(many=True)
    order_id = serializers.CharField(read_only = True)
    total_amount = serializers.DecimalField(read_only=True, max_digits=12,decimal_places=2)
    
    class Meta:
        model = Order 
        fields = ['address','zip_code','items','total_amount','order_id']
        
    
    def validate(self, attrs):
        
        if len(attrs['items']) < 1:
            raise serializers.ValidationError(
                'Order must contain at least one item.'
            )
        
        return super().validate(attrs)
        
    
    @transaction.atomic
    def create(self, validated_data):
        
        validated_data['user'] = self.context['request'].user
        
        items_data = validated_data.pop("items")
        
        order = Order.objects.create(total_amount = 0, **validated_data)
        
        total = Decimal("0.00")
        
        
        for item in items_data:
            product = item['product']
            qty = item['quantity']
            
            unit_price = product.price
            
            if product.is_offered:
                discount = unit_price * Decimal(product.percent_offer) / 100
                unit_price -= discount
            
            
            total += unit_price * qty
            
            OrderItem.objects.create(order = order, product = product, quantity = qty, amount = unit_price * qty)
            
            # decrease stock
            product.stock -= qty
            product.save(update_fields=['stock'])
            
        order.total_amount = total
        order.save(update_fields = ['total_amount'])
        
        return order
        