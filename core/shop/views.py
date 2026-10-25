from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializers import ProductSerializer, CategorySerializer
from .models import Category , Product
from .filters import ProductFilter

# Create your views here.

class CategoryListApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListApi(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
            
    
class ProductDetailApi(RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializer