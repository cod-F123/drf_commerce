from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product


User = get_user_model()

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    replyed = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="replies")
    
    content = models.TextField()
    
    date_created = models.DateTimeField(auto_now_add=True)
    depth = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        ordering = ['date_created']
    
    
    def save(self, *args, **kwargs):
        
        if self.replyed:
            self.depth = self.replyed.depth + 1
        
        else:
            self.depth = 0
        
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.user.username} commented to {self.product.name}"