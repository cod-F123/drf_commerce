from django.shortcuts import render
from rest_framework.generics import CreateAPIView , DestroyAPIView , UpdateAPIView
from rest_framework.permissions import IsAuthenticated 
from .permissions import IsOwnerComment , CanDeletePermission , CanUpdatePermission
from .models import Comment
from .serializers import CreateCommentSerializer , UpdateCommentSerializer
from .utils import get_comment_setting

# Create your views here.

class CreateCommentApi(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]
    
    
class DeleteCommentApi(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerComment, CanDeletePermission]
    lookup_field = "id"

class UpdateCommentApi(UpdateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerComment, CanUpdatePermission]
    serializer_class =  UpdateCommentSerializer
    lookup_field = "id"