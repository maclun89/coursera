from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Manager').exists() or request.user.is_superuser:
            return True


class IsDeliveryCrew(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Delivery crew').exists() or request.user.is_superuser:
            return True
