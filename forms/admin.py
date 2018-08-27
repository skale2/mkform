from django.contrib import admin
from forms.models.base import (
    Form,
    Response,
)
from forms.models.field_defs import (
    ShortAnswerDef,
    LongAnswerDef,
    NumberDef,
    BooleanDef,
    ChoiceDef,
    MultipleChoiceDef,
    CheckboxDef,
    MultipleChoiceGridDef,
    CheckboxGridDef,
    DateDef,
    TimeDef,
    DateTimeDef,
    FileDef,
)
from forms.models.fields import (
    ShortAnswer,
    LongAnswer,
    Number,
    Boolean,
    Choice,
    MultipleChoice,
    Checkbox,
    Date,
    Time,
    DateTime,
    File,
)
from forms.models.permissions import (
    FormPermission,
    ResponsePermission,
)
from forms.models.validators import (
    SizeValidator,
    DateValidator,
    TimeValidator,
    DateTimeValidator,
    BooleanValidator,
    RegexValidator,
    FileValidator,
)
# Register your models here.

admin.site.register(Form)
admin.site.register(Response)

admin.site.register(ShortAnswerDef)
admin.site.register(LongAnswerDef)
admin.site.register(NumberDef)
admin.site.register(BooleanDef)
admin.site.register(ChoiceDef)
admin.site.register(MultipleChoiceDef)
admin.site.register(CheckboxDef)
admin.site.register(MultipleChoiceGridDef)
admin.site.register(CheckboxGridDef)
admin.site.register(DateDef)
admin.site.register(TimeDef)
admin.site.register(DateTimeDef)
admin.site.register(FileDef)

admin.site.register(ShortAnswer)
admin.site.register(LongAnswer)
admin.site.register(Number)
admin.site.register(Boolean)
admin.site.register(Choice)
admin.site.register(MultipleChoice)
admin.site.register(Checkbox)
admin.site.register(Date)
admin.site.register(Time)
admin.site.register(DateTime)
admin.site.register(File)

admin.site.register(FormPermission)
admin.site.register(ResponsePermission)

admin.site.register(SizeValidator)
admin.site.register(DateValidator)
admin.site.register(TimeValidator)
admin.site.register(DateTimeValidator)
admin.site.register(BooleanValidator)
admin.site.register(RegexValidator)
admin.site.register(FileValidator)