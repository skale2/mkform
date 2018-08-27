from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import permissions
from forms.models.base import (
    Form, 
    Response,
)
from forms.const import (
    MANAGE,
    EDIT,
    RESPOND,
    VIEW,
    NONE,
)
from forms.models.permissions import (
    UserPermission,
    FormPermission,
    ResponsePermission,
)

def has_permission(request, obj, level):
    if isinstance(obj, User):
        permission_class = UserPermission
    if isinstance(obj, Form):
        permission_class = FormPermission
    elif isinstance(obj, Response):
        permission_class = ResponsePermission
    
    return permission_class.is_permitted(
        user=request.user,
        obj=obj,
        level=level,
    )[0]


class CanManagePermission(permissions.BasePermission):
    """
    Request can manage a resource
    """
    def has_object_permission(self, request, view, obj):
        return has_permission(request, obj, MANAGE)


class CanEditPermission(permissions.BasePermission):
    """
    Request can manage a resource
    """
    def has_object_permission(self, request, view, obj):
        return has_permission(request, obj, EDIT)


class CanRespondPermission(permissions.BasePermission):
    """
    Request can manage a resource
    """
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Response):
            return False
        return has_permission(request, obj, RESPOND)


class CanViewPermission(permissions.BasePermission):
    """
    Request can manage a resource
    """
    def has_object_permission(self, request, view, obj):
        return has_permission(request, obj, VIEW)