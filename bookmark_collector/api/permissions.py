from django.core.handlers.wsgi import WSGIRequest
from rest_framework import permissions
from rest_framework.routers import APIRootView


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return request.method in permissions.SAFE_METHODS


class BlockPermission(permissions.BasePermission):
    def has_permission(self, request: WSGIRequest, view: APIRootView):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_active
        )


class AdminOrReadOnly(BlockPermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.role == "admin":
            return True
