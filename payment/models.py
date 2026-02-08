from django.db import models
from orders.models import Order

# Create your models here.


class Transaction(models.Model):
    
    STATUS = (
        ('PENDING','PENDING'),
        ('SUCCESS','SUCCESS'),
        ('FAIL','FAIL')
    )
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    ref_id = models.CharField(blank=True, null=True,max_length=255)
    
    
    authority_id = models.CharField(max_length=255, blank=True, null=True)
    
    transaction_status = models.CharField(max_length=10, choices=STATUS, default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        
        if not self.amount:
            self.amount = self.order.total_amount
    
        super().save(*args, **kwargs)
    
    
    
    
    