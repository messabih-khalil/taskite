from rest_framework import permissions


class IsUser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

            
class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.admin == request.user:
            return True

