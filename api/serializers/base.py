from django.contrib.auth.models import User
from rest_framework import serializers
from forms.const import (
    MANAGE,
    VIEW,
    EDIT,
    RESPOND,
    NONE,
)
from forms.models.base import (
    Form,
    Response,
)
from forms.models.permissions import (
    FormPermission,
    ResponsePermission,
)


DEFAULT_FIELDS = ['name', 'creator', 'created', 'permission']

class ShortSerializer(serializers.ModelSerializer):
    permission = serializers.SerializerMethodField()

    def get_permission(self, obj):
        user, request = None, self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return self.permission_class.is_permitted(user, obj, VIEW)[0] if user else False


class FormShortSerializer(ShortSerializer):
    permission_class = FormPermission

    responses = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = DEFAULT_FIELDS + ['responses', 'questions']

    def get_responses(self, obj):
        return obj.num_responses

    def get_questions(self, obj):
        return obj.num_questions


class ResponseShortSerializer(serializers.Serializer):
    permission_class = ResponsePermission

    class Meta:
        model = Response
        fields = DEFAULT_FIELDS



class FormSerializer(serializers.Serializer):
    class Meta:
        model = Form
        fields = '__all__'
        depth = 2
        read_only_fields = ('created',)


class ResponseSerializer(serializers.Serializer):
    class Meta:
        model = Response
        fields = '__all__'
        depth = 1
        read_only_fields = ('created',)


class ActivitySerializer(serializers.ModelSerializer):
    forms = FormShortSerializer(many=True)
    responses = ResponseShortSerializer(many=True)

    class Meta:
        model = User
        fields = ('forms', 'responses')
        depth = 2

