from rest_framework.permissions import BasePermission, SAFE_METHODS

from api_users.models import Role


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser


class IsAuthorOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        user = request.user
        if user.is_admin or user.role == Role.MODERATOR :
            return True

        return obj.author == user
