from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from forms.const import (
    MANAGE,
    EDIT,
    RESPOND,
    VIEW,
    NONE,
)
from forms.models.base import (
    Base,
    Form,
    Response,
)


class Permission(Base):
    """
    A permission relation between a resource and a user, detailing if 
    the user can access the resource in different ways
    """
    class Meta:
        abstract = True
    
    expiration = models.DateTimeField()

    @staticmethod
    def this_query(obj):
        return {}

    @staticmethod
    def get_object(pk):
        return None
    
    @classmethod
    def is_permitted_id(cls, user_id, obj_id, level, create=False):
        return cls.is_permitted(
            user=User.objects.get(id=user_id),
            obj=cls.get_object(obj_id),
            level=level,
            create=create,
        )

    @classmethod
    def is_permitted(cls, user, obj, level, create=False, expiration=datetime.max):
        def _is_permitted(permission, level):
            return permission.level <= level and datetime.now() < permission.expiration

        try:
            permission = cls.objects.get(user=user, **cls.this_query(obj))
            if not _is_permitted(permission, level) and create:
                permission = cls.objects.create(
                    user=user,
                    level=obj.default_permission,
                    expiration=expiration, 
                    **cls.this_query(obj)
                )
                return True, permission
            return _is_permitted(permission, level), None
        except cls.DoesNotExist:
            if create:
                permission = cls.objects.create(
                    user=user,
                    level=obj.default_permission,
                    expiration=expiration, 
                    **cls.this_query(obj)
                )
                return _is_permitted(permission, level), permission
            return obj.default_permission <= level, None


class UserPermission(Permission):
    LEVELS = (
        (MANAGE, 'Manage'),  # Can manage (delete, assign priviledges, etc.)
        (VIEW, 'View'),  # Can view activity
        (NONE, 'None'),
    )

    LEVELS_DICT = dict(LEVELS)

    user = models.ForeignKey(to=User, related_name='user_permissions', on_delete=models.CASCADE)
    to_user = models.ForeignKey(to=user, related_name='to_user_permissions', on_delete=models.CASCADE)
    level = level = models.SmallIntegerField(choices=LEVELS, default=VIEW)

    @staticmethod
    def this_query(obj):
        return {'user': obj}

    @staticmethod
    def get_object(pk):
        return User.objects.get(id=pk)


class FormPermission(Permission):
    LEVELS = (
        (MANAGE, 'Manage'),  # Can rename, delete, duplicate, or transfer ownership
        (EDIT, 'Edit'),
        (RESPOND, 'Respond'),
        (VIEW, 'View'),
        (NONE, 'None'),
    )

    LEVELS_DICT = dict(LEVELS)

    user = models.ForeignKey(to=User, related_name='form_permissions', on_delete=models.CASCADE)
    form = models.ForeignKey(to=Form, on_delete=models.CASCADE)
    level = models.SmallIntegerField(choices=LEVELS, default=RESPOND)

    @staticmethod
    def this_query(obj):
        return {'form': obj}

    @staticmethod
    def get_object(pk):
        return Form.objects.get(id=pk)

class ResponsePermission(Permission):
    LEVELS = (
        (MANAGE, 'Manage'),  # Can delete
        (EDIT, 'Edit'),
        (VIEW, 'View'),
        (NONE, 'None'),
    )

    LEVELS_DICT = dict(LEVELS)

    user = models.ForeignKey(to=User, related_name='response_permissions', on_delete=models.CASCADE)
    response = models.ForeignKey(to=Response, on_delete=models.CASCADE)
    level = models.SmallIntegerField(choices=LEVELS, default=VIEW)

    @staticmethod
    def this_query(obj):
        return {'response': obj}

    @staticmethod
    def get_object(pk):
        return Response.objects.get(id=pk)