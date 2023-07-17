from rest_framework.permissions import BasePermission


class IsDeckOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class OnlyAdminCanPost(BasePermission):
    def has_permission(self, request, view):
        return request.method != 'POST' or permissions.IsAdminUser().has_permission(request, view)
