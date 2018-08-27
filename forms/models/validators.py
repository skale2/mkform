import re
import sys
import datetime
import magic
from django.db import models
from django.core.files import File
from picklefield.fields import PickledObjectField
from forms.models.base import (
    Base,
)


class InvalidFieldException(Exception):
    pass


class Validator(Base):
    """
    A validator based on certain parameters
    """
    class Meta:
        abstract = True

    DEFAULT_MESSAGE = "Internal Error: This validator is abstract"

    message = models.CharField(max_length=255, default=DEFAULT_MESSAGE)

    def validate(self, value):
        self.error()

    def error(self, **params):
        raise InvalidFieldException(self.message.format(params))


class SizeValidator(Validator):
    DEFAULT_MESSAGE = "{value} can't be {cmpr} {constraint}"
    
    max_size = models.IntegerField(default=sys.maxsize)
    min_size = models.IntegerField(default=-sys.maxsize)

    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"

    def validate(self, value):
        if isinstance(value, str):
            value = len(value)

        if value > self.max_size:
            self.error(
                value=value,
                cmpr=self.GREATER_THAN,
                constraint=self.max_size,
            )
        if value < self.min_size:
            self.error(
                value=value,
                cmpr=self.LESS_THAN,
                constraint=self.min_size,
            )


class DateValidator(SizeValidator):
    max_date = models.DateField(default=datetime.date.max)
    min_date = models.DateField(default=datetime.date.min)

    GREATER_THAN = "after"
    LESS_THAN = "before"
    
    @property
    def max_size(self):
        return self.max_date

    @property
    def min_size(self):
        return self.min_date

    def validate(self, value):
        if not isinstance(value, datetime.date):
            raise InvalidFieldException("value is not a python date")
        
        super().validate(value)


class TimeValidator(SizeValidator):
    max_time = models.TimeField(default=datetime.time.max)
    min_time = models.TimeField(default=datetime.time.min)

    GREATER_THAN = "after"
    LESS_THAN = "before"
    
    @property
    def max_size(self):
        return self.max_time

    @property
    def min_size(self):
        return self.min_time

    def validate(self, value):
        if not isinstance(value, datetime.time):
            raise InvalidFieldException("value is not a python time")
        super().validate(value)


class DateTimeValidator(SizeValidator):
    max_datetime = models.DateTimeField(default=datetime.datetime.max)
    min_datetime = models.DateTimeField(default=datetime.datetime.min)

    GREATER_THAN = "after"
    LESS_THAN = "before"
    
    @property
    def max_size(self):
        return self.max_datetime

    @property
    def min_size(self):
        return self.min_datetime

    def validate(self, value):
        if not isinstance(value, datetime.datetime):
            raise InvalidFieldException("value is not a python datetime")
        super().validate(value)


class BooleanValidator(Validator):
    DEFAULT_MESSAGE = "this value must be {must_be}"

    must_be = models.BooleanField()

    def validate(self, value):
        if not isinstance(value, bool):
            raise InvalidFieldException("Value is not a python boolean")

        if value is not self.must_be:
            self.error(must_be=self.must_be)


class RegexValidator(Validator):
    DEFAULT_MESSAGE = "{value} does not match {pattern}"

    regex = models.CharField(max_length=255)
    contains = models.BooleanField(default=True)

    def validate(self, value):
        if not isinstance(value, str):
            raise InvalidFieldException("Value is not a python string")

        if re.compile(self.regex).match(value) is self.contains:
            self.error(
                value=value,
                pattern=self.regex,
            )


class FileValidator(SizeValidator):
    FILE_TYPES = (
        ('text/plain',                  'Plain Text'    ),
        ('text/html',                   'HTML'          ),
        ('text/css',                    'CSS'           ),
        ('text/javascript',             'Javascript'    ),
        ('image/gif',                   'GIF'           ),
        ('image/png',                   'PNG'           ),
        ('image/png',                   'PNG'           ),
        ('image/jpeg',                  'JPEG'          ),
        ('image/bmp',                   'BMP'           ),
        ('image/webp',                  'WEBP'          ),
        ('audio/midi',                  'MIDI'          ),
        ('audio/mpeg',                  'MPEG'          ),
        ('audio/webm',                  'WEBM'          ),
        ('audio/ogg',                   'OGG'           ),
        ('audio/wav',                   'WAV'           ),
        ('video/webm',                  'WEBM'          ),
        ('video/ogg',                   'OGG'           ),
        ('application/octet-stream',    'Octet Stream'  ),
        ('application/pkcs12',          'PKCS12'        ),
        ('application/vnd.mspowerpoint','MS Powerpoint' ),
        ('application/xhtml+xml',       'XHTML XML'     ),
        ('application/xml',             'XML'           ),
        ('application/pdf',             'PDF'           ),
        ('multipart/form-data',         'Form Data'     ),
    )

    FILE_TYPES_MAP = dict(FILE_TYPES)

    accepted_types = PickledObjectField()
    
    max_bytes = models.BigIntegerField(default=1e7)
    min_bytes = models.BigIntegerField(default=0)

    @property
    def max_size(self):
        return self.max_bytes

    @property
    def min_size(self):
        return self.min_bytes

    GREATER_THAN = "bigger than"
    LESS_THAN = "smaller than"

    def validate(self, value):
        if not isinstance(value, File):
            raise InvalidFieldException("value is not a file")

        file_type = magic.from_file(value, mime=True)
        if file_type not in self.accepted_types:
            raise InvalidFieldException("value can't be of type {}".format(file_type))

        super().validate(value)