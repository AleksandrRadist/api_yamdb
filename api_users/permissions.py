from rest_framework import permissions
from .models import Role


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.role == Role.ADMIN or request.user.is_staff:
            return True
        return request.user.is_staff
