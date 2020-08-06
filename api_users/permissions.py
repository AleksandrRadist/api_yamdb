from rest_framework import permissions


class IsStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):


        if request.user.role == 'admin':
            return True

        if request.user.is_staff:
            return True

        return request.user.is_staff
