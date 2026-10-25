from rest_framework.permissions import BasePermission
from .utils import get_order_settings

class CanDeleteOrder(BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method == 'DELETE':
            return get_order_settings('USER_CAN_DELETE_ORDER',False)
        
        return super().has_permission(request, view)