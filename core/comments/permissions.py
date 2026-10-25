from rest_framework.permissions import BasePermission
from .utils import get_comment_setting

class IsOwnerComment(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id 
    
class CanDeletePermission(BasePermission):
    
    def has_permission(self, request, view):
        return  get_comment_setting("USER_CAN_DELETE",False)

class CanUpdatePermission(BasePermission):
    
    def has_permission(self, request, view):
        return  get_comment_setting("USER_CAN_UPDATE",False)