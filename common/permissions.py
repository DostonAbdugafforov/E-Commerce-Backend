from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and
                request.user.role == 'admin'
        )


class IsAdminOrSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and
                request.user.role in ['admin', 'seller']
        )


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return True

        return obj.owner == request.user
