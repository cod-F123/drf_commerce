from rest_framework.permissions import BasePermission

class IsCorrectUser(BasePermission):
    
    def has_object_permission(self, request, view, obj):

        return request.user.email == obj.email
    
    
class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.user.email
