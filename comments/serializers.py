from rest_framework import serializers
from .utils import get_comment_setting
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Comment
        fields = "__all__"
    
    def get_replies(self, obj):
        max_depth = get_comment_setting('MAX_DEPTH',3)
        
        if obj.depth >= max_depth:
            return []
        
        serializer = CommentSerializer(obj.replies.all(),many=True, context = self.context)
        
        return serializer.data

class CreateCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["product","content","replyed"]
    
    def validate(self, attrs):
        
        replyed = attrs.get('replyed')
        max_depth = get_comment_setting('MAX_DEPTH',3)
        allowed_nested_reply = get_comment_setting('ALLOWED_NESTED_REPLY',False)
        
        if not allowed_nested_reply and replyed.depth >= 1 :
            raise serializers.ValidationError("Not ALLOWED NESTED REPLY !")
        
        if replyed and replyed.depth >= max_depth :
            raise serializers.ValidationError("Maximun Reply DEPTH ERROR !")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class UpdateCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["content"]