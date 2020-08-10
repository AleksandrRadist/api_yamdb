from rest_framework import permissions


class IsStaff(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.role == 'admin':
            return True

        elif request.user.is_staff:
            return True

        elif request.user.role != 'admin':
            return False

        return request.user.is_staff
