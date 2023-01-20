from django.db import models
from django.http import HttpRequest
from rest_framework import permissions
from rest_framework import viewsets


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(
        self,
        request: HttpRequest,
        view: viewsets.ModelViewSet,
        obj: models.Model,
    ) -> bool:
        del view
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
        )
