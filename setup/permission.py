from rest_framework import permissions


class IsDeckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class OnlyAdminCanPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method != 'POST' or permissions.IsAdminUser().has_permission(request, view)
