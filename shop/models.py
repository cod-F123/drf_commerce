from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from tinymce import models as tiny_models
import uuid

# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to="upload/category")
    
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["id"]
    
    def __str__(self):
        return self.name
    
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="upload/product")
    description = tiny_models.HTMLField(blank=True,null=True)
    
    is_exist = models.BooleanField(default=True)
    percent_off = models.IntegerField(default=0)
    
    slug = models.CharField(max_length=255, blank=True, null=True, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    stock = models.PositiveBigIntegerField(default=0)
    
    
    @property
    def is_offered(self):
        return self.percent_off > 0
    
    @property
    def offered_price(self):
        return self.price - (self.price * self.percent_off)
    
    def save(self, *args, **kwargs):
        
        if self.slug is None:
            self.slug = str(uuid.uuid4()).replace("-","") + str(timezone.now().microsecond)
        
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    class Meta:
        ordering = ["-date_added"]


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="upload/gallery/product")
    
    def __str__(self):
        return self.product.name
    