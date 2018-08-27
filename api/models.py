import re
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


VALID_PASSWORD = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])"
MIN_PASSWORD_LEN = 6

class AuthError(Exception):
    MISSING_FIELDS = 'please provide both username and password'
    INVALID_CREDENTIALS = 'invalid Credentials'
    PASSWORD_TOO_SHORT = 'password must be at least {} characters long'.format(MIN_PASSWORD_LEN)
    DISALLOWED_CHARACTERS = 'password must have at least on lowercase letter one uppercase letter, one number, and one special character'
    UNMATCHING_PASSWORDS = 'unmatching passwords'
    MATCHING_PASSWORDS = 'new password cannot be the same as old password'
    USER_EXISTS = 'user already exists'
    USER_DOES_NOT_EXIST = 'user does not exist'

    @classmethod
    def missing_fields(cls):
        raise cls(cls.MISSING_FIELDS)
    
    @classmethod
    def invalid_credentials(cls):
        raise cls(cls.INVALID_CREDENTIALS)

    @classmethod
    def password_too_short(cls):
        raise cls(cls.PASSWORD_TOO_SHORT)

    @classmethod
    def disallowed_characters(cls):
        raise cls(cls.DISALLOWED_CHARACTERS)

    @classmethod
    def unmatching_passwords(cls):
        raise cls(cls.UNMATCHING_PASSWORDS)

    @classmethod
    def matching_passwords(cls):
        raise cls(cls.MATCHING_PASSWORDS)

    @classmethod
    def user_exists(cls):
        raise cls(cls.USER_EXISTS)

    @classmethod
    def user_does_not_exist(cls):
        raise cls(cls.USER_DOES_NOT_EXIST)


def _check_password(password):
    if len(password) < MIN_PASSWORD_LEN:
        AuthError.password_too_short()

    if not re.match(VALID_PASSWORD, password):
        AuthError.disallowed_characters()

def _create_user(username, password, confirm_password):
    if username is None or password is None or confirm_password is None:
        AuthError.missing_fields()

    user = User.objects.filter(username=username)
    if user:
        AuthError.user_exists()

    _check_password(password)

    if password != confirm_password:
        AuthError.unmatching_passwords()

    user = User.objects.create(
        username=username,
        password=password,
    )

    return user

def _authenticate(username, password):
    if username is None or password is None:
        AuthError.missing_fields()

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        AuthError.user_does_not_exist()

    if not user.check_password(password):
        AuthError.invalid_credentials()

    return user

def _change_password(username, password, new_password):
    user = _authenticate(username, password)

    _check_password(new_password)

    if password == new_password:
        AuthError.matching_passwords()

    user.set_password(password)
    user.save()

    return user
