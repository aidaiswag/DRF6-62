from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if not request.user.is_staff:
            return False
        if request.method == 'POST':
            return False
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True


