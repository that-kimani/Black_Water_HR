from rest_framework.permissions import BasePermission

class IsHRUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.employee_class == 'hr'