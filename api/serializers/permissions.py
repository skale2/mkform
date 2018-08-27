from datetime import datetime
from rest_framework import serializers
from forms.models.permissions import (
    UserPermission,
    FormPermission,
    ResponsePermission,
)

class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'
        
class FormPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormPermission
        fields = '__all__'

class ResponsePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsePermission
        fields = '__all__'


class UserGivePermissionSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserPermission)
    level = serializers.ChoiceField(choices=UserPermission.LEVELS)
    expiration = serializers.DateTimeField(default=datetime.max)

    def create(self, validated_data, user):
        return UserPermission.objects.update_or_create(
            user=user,
            to_user=validated_data.get("user"),
            level=validated_data.get("level"),
            expiration=validated_data.get("expiration"),
        )[0]