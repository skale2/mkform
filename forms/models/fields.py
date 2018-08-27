from django.db import models
from django.contrib.auth.models import User
from forms.models.base import (
    Base,
    Form,
    Response,
)
from forms.models.validators import (
    FileValidator,
)
from forms.models.field_defs import (
    FieldDef,
    ShortAnswerDef,
    LongAnswerDef,
    NumberDef,
    BooleanDef,
    DateDef,
    TimeDef,
    DateTimeDef,
    ChoiceDef,
    MultipleChoiceDef,
    MultipleChoiceGridDef,
    FileDef,
)

class Field(Base):
    """
    A single field from a response, corresponding to a field definition
    on the form
    """
    class Meta:
        abstract = True

    form = models.ForeignKey(to=Form, on_delete=models.CASCADE)
    response = models.ForeignKey(to=Response, on_delete=models.CASCADE)

    def validate(self):
        self.definition.validate(self.value)

class ShortAnswer(Field):
    definition = models.ForeignKey(to=ShortAnswerDef, on_delete=models.CASCADE)
    value = models.CharField(max_length=ShortAnswerDef.REAL_MAX)

class LongAnswer(Field):
    definition = models.ForeignKey(to=LongAnswerDef, on_delete=models.CASCADE)
    value = models.TextField()

class Number(Field):
    definition = models.ForeignKey(to=NumberDef, on_delete=models.CASCADE)
    value = models.IntegerField()

class Boolean(Field):
    definition = models.ForeignKey(to=BooleanDef, on_delete=models.CASCADE)
    value = models.NullBooleanField()

class Choice(Field):
    definition = models.ForeignKey(to=ChoiceDef, on_delete=models.CASCADE)
    value = models.ForeignKey(to=Boolean, on_delete=models.CASCADE)
    multiple_choice = models.ForeignKey(to="MultipleChoice", related_name="choices", on_delete=models.CASCADE)

class MultipleChoice(Field):
    grid = models.ForeignKey(to="MultipleChoiceGrid", related_name="choice_rows", on_delete=models.CASCADE)
    definition = models.ForeignKey(to=MultipleChoiceDef, on_delete=models.CASCADE)

class MultipleChoiceGrid(Field):
    definition = models.ForeignKey(to=MultipleChoiceGridDef, on_delete=models.CASCADE)

class Date(Field):
    definition = models.ForeignKey(to=DateDef, on_delete=models.CASCADE)
    value = models.DateField()

class Time(Field):
    definition = models.ForeignKey(to=TimeDef, on_delete=models.CASCADE)
    value = models.TimeField()

class DateTime(Field):
    definition = models.ForeignKey(to=DateTimeDef, on_delete=models.CASCADE)
    value = models.DateTimeField()

class File(Field):
    definition = models.ForeignKey(to=FileDef, on_delete=models.CASCADE)
    value = models.FileField()
    mimetype = models.CharField(max_length=30, choices=FileValidator.FILE_TYPES)