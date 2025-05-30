from rest_framework import permissions

class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()

class IsProjectManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.manager == request.user

class IsAssigneeOrManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assignee == request.user or obj.project.manager == request.user