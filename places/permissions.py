from django.contrib.auth.models import User
from rest_framework import permissions


class OwnProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user == User.objects.get(
            pk=request.query_params.get('id'))
