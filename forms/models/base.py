from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import User
from forms.const import (
    MANAGE,
    EDIT,
    RESPOND,
    VIEW,
    NONE,
    FIELD_TYPES,
)
from forms.exceptions import (
    RespondingError,
)


class Base(models.Model):
    """
    A base model containing basic information for every object
    persisted in the database
    """
    class Meta:
        abstract = True

    creator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Form(Base):
    """
    A form, containing one or more fields
    """
    LEVELS = (
        (MANAGE, 'Manage'),  # Can rename, delete, duplicate, or transfer ownership
        (EDIT, 'Edit'),
        (RESPOND, 'Respond'),
        (VIEW, 'View'),
    )

    desc = models.TextField(null=True, blank=True)
    default_permission = models.IntegerField(choices=LEVELS, default=RESPOND)
    accepting_responses = models.BooleanField(default=True)

    @cached_property
    def num_responses(self):
        return len(self.response_set.all())

    @cached_property
    def num_questions(self):
        return len(self.field_defs.all())

    def respond(self, response):
        """ Attaches a response to this form, validating each of its fields,
            and marking it valid if it is

            args:
                response:Response 
            throws: 
                InvalidFieldException
        """
        if not self.accepting_responses:
            RespondingError.not_accepting_responses()
        
        for field_type in FIELD_TYPES:
            fields = getattr(response, "{}_set".format(field_type))
            for field in fields:
                field.validate()
            
        response.valid = True
        response.save()


class Response(Base):
    """
    A single response to a form
    """
    LEVELS = (
        (MANAGE, 'Manage'),  # Can delete
        (EDIT, 'Edit'),
        (VIEW, 'View'),
    )

    form = models.ForeignKey(to=Form, on_delete=models.CASCADE)
    default_permission = models.IntegerField(choices=LEVELS, default=VIEW)
    valid = models.BooleanField(default=False)
