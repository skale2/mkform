import sys
from django.db import models
from django.contrib.auth.models import User
from forms.models.base import (
    Base,
    Form,
)
from forms.models.validators import (
    InvalidFieldException,
    SizeValidator,
    RegexValidator,
    BooleanValidator,
    DateValidator,
    TimeValidator,
    DateTimeValidator,
    FileValidator,
)


class FieldDef(Base):
    """
    A field definition, along with associated validators, attached
    to a form.
    """
    class Meta:
        abstract = True

    form = models.ForeignKey(
        to=Form,
        related_name='fields_defs',
        on_delete=models.CASCADE,
    )
    desc = models.TextField(null=True, blank=True)
    required = models.BooleanField(default=False)

    VALIDATORS = []

    def validate(self, value):
        """ args:
                value:Any python repr of value to be validated
            throws: 
                InvalidFieldException
        """
        for validator_name in self.VALIDATORS:
            validator = getattr(self, validator_name)
            if validator:
                validator.validate(value)


class ShortAnswerDef(FieldDef):
    REAL_MAX = 255
    REAL_MIN = 0

    VALIDATORS = ["size_validator", "regex_validator"]

    size_validator = models.OneToOneField(
        to=SizeValidator, 
        on_delete=models.CASCADE
    )
    regex_validator = models.OneToOneField(
        to=RegexValidator, 
        on_delete=models.CASCADE
    )


class LongAnswerDef(FieldDef):
    REAL_MAX = sys.maxsize
    REAL_MIN = 0

    VALIDATORS = ["size_validator", "regex_validator"]

    size_validator = models.OneToOneField(
        to=SizeValidator, 
        on_delete=models.CASCADE
    )
    regex_validator = models.OneToOneField(
        to=RegexValidator, 
        on_delete=models.CASCADE
    )


class NumberDef(FieldDef):
    REAL_MAX = sys.maxsize
    REAL_MIN = -sys.maxsize

    VALIDATORS = ["size_validator"]

    size_validator = models.OneToOneField(
        to=SizeValidator, 
        on_delete=models.CASCADE
    )


class BooleanDef(FieldDef):
    VALIDATORS = ["boolean_validator"]

    boolean_validator = models.OneToOneField(
        to=BooleanValidator, 
        on_delete=models.CASCADE
    )


class ChoiceDef(BooleanDef):
    multiple_choice = models.ForeignKey(
        to="MultipleChoiceDef", 
        related_name="choices", 
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )
    checkbox = models.ForeignKey(
        to="CheckboxDef", 
        related_name="choices", 
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )


class MultipleChoiceDef(FieldDef):
    grid = models.ForeignKey(
        to="MultipleChoiceGridDef", 
        related_name="multiple_choices", 
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
    )
    single = models.BooleanField(default=False)

    def validate(self, value):
        """
        args:
            value:bool[] Describes choices selected
        """
        chosen = False
        for i, choice in enumerate(ChoiceDef.objects.filter(multiple_choice=self)):
            if self.single and value[i]:
                if chosen:
                    raise InvalidFieldException("only one choice can be made")
                chosen = True
            choice.validate(value[i])


class MultipleChoiceGridDef(FieldDef):
    def validate(self, value):
        """
        args:
            value:bool[][] Describes choices selected
        """
        # TODO: fix!
        for choice in ChoiceDef.objects.filter(multiple_choice__grid=self):
            choice.validate(value)


class DateDef(FieldDef):
    VALIDATORS = ["date_validator"]

    date_validator = models.OneToOneField(to=DateValidator, on_delete=models.CASCADE)


class TimeDef(FieldDef):
    VALIDATORS = ["time_validator"]

    time_validator = models.OneToOneField(to=TimeValidator, on_delete=models.CASCADE)


class DateTimeDef(FieldDef):
    VALIDATORS = ["datetime_validator"]

    datetime_validator = models.OneToOneField(to=DateTimeValidator, on_delete=models.CASCADE)


class FileDef(FieldDef):
    VALIDATORS = ["file_validator"]

    file_validator = models.OneToOneField(to=FileValidator, on_delete=models.CASCADE)