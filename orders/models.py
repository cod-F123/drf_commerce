from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid
from accounts.models import UserAddress
from shop.models import Product


User = get_user_model()

# Create your models here.

class Order(models.Model):
    
    STATUS = (
        ('Pending','Pending'),
        ('Payed','Payed'),
        ('Proccessing','Proccessing'),
        ('Shipped','Shipped')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.TextField()
    zip_code = models.CharField(max_length=15)
    
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    order_status = models.CharField(max_length=11,choices=STATUS, default='Pending')
    
    created_at  = models.DateTimeField(auto_now_add=True)
    payed_at = models.DateTimeField(blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    
    order_id = models.CharField(blank=True, null=True)
    
    
    class Meta:
        ordering = ['-created_at']
    
    
    def save(self, *args, **kwargs):
        
        if self.order_id is None:
            self.order_id = str(uuid.uuid4()).replace('-','')[:5] + str(timezone.now().microsecond)
        
        if (self.order_status == 'Payed' or self.order_status == 'Proccessing') and self.payed_at is None:
            self.payed_at = timezone.now()
        
        if self.order_status == 'Shipped' and self.shipped_at is None:
            self.shipped_at = timezone.now()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.email} - {self.total_amount} - {self.order_status} - created at {self.created_at}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.order.order_id} - {self.product.name} {self.quantity}"
    