from rest_framework import serializers
from .models import Category , Product , ImageProduct
from comments.serializers import CommentSerializer

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["name","image"]
    


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ["image","id"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True) 
    comments = serializers.SerializerMethodField()
    gallery = ImageProductSerializer(many=True)
    
    class Meta:
        model = Product
        fields = "__all__"
        
    def get_comments(self, obj):
        return CommentSerializer(
            obj.comments.filter(depth=0),
            many=True,
            context=self.context
        ).data
