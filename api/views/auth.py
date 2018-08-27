from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets
from rest_framework.decorators import action
from forms.const import (
    MANAGE,
    EDIT,
    RESPOND,
    VIEW,
    NONE,
)
from forms.models.base import (
    Form,
    Response,
)
from forms.models.permissions import (
    FormPermission,
    ResponsePermission,
    UserPermission,
)
from api.serializers.base import (
    ActivitySerializer,
)
from api.serializers.permissions import (
    FormPermissionSerializer,
    ResponsePermissionSerializer,
    UserPermissionSerializer,
    UserGivePermissionSerializer,
)
from api.permissions import (
    CanEditPermission,
    CanManagePermission,
    CanRespondPermission,
    CanViewPermission,
)
from api.models import (
    AuthError,
    _authenticate,
    _create_user,
    _change_password,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    @action(
        methods=['post'],
        detail=False,
        permission_classes=(AllowAny,)
    )
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = _authenticate(username, password)
        except AuthError as ae:
            return Response({'error': str(ae)},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'token': user.token.key},
                        status=status.HTTP_200_OK)

    @action(
        methods=['post'],
        detail=False,
        permission_classes=(AllowAny,),
    )
    def create(self, request):    
        username = request.data.get("username")
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")

        try:
            user = _create_user(username, password, confirm_password)
        except AuthError as ae:
            return Response({'error': str(ae)},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'token': user.token.key},
                        status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=False,
        permission_classes=(AllowAny,),
    )
    def change_password(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        new_password = request.data.get("new_password")

        try:
            user = _change_password(username, password, new_password)
        except AuthError as ae:
            return Response({'error':str(ae)},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'password changed'},
                        status=status.HTTP_200_OK)

    @action(
        methods=['get'],
        detail=True,
        permission_classes=(TokenAuthentication, CanViewPermission),
    )
    def activity(self, request, pk):
        try:
            serializer = ActivitySerializer(User.objects.get(pk=pk))
        except User.DoesNotExist:
            return Response({'failure': AuthError.USER_DOES_NOT_EXIST},
                            status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['post'], 
        detail=True,
        permission_classes=(TokenAuthentication, CanViewPermission,),
    )
    def give_permission(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'failure': AuthError.USER_DOES_NOT_EXIST},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = UserGivePermissionSerializer(request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.create(
            validated_data=serializer.validated_data,
            user=user,
        )
        return Response({'success': 'permissions given'},
                        status=status.HTTP_200_OK)

    @action(
        methods=['post'], 
        detail=True,
        permission_classes=(TokenAuthentication, CanManagePermission),
    )
    def change_permission(self, request, pk=None):
        if "form" in request.data:
            serializer_class = FormPermissionSerializer
            permission_class = FormPermission
            field = "form"
        elif "response" in request.data:
            serializer_class = ResponsePermissionSerializer
            permission_class = ResponsePermission
            field = "response"
        elif "user" in request.data:
            serializer_class = UserPermissionSerializer
            permission_class = UserPermission
            field = "response"
        else: 
            return Response({'failure': 'provide an resource to add permissions to'},
                            status=status.status.HTTP_400_BAD_REQUEST)
        
        # Try to deserialize the data
        serializer = serializer_class({"user": pk, **request.data})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if request user is allowed to manage this resource
        is_permitted, _ = permission_class.is_permitted_id(
            user_id=request.user.id,
            obj_id=serializer.validated_data.get(field),
            level=MANAGE,
        )

        if not is_permitted:
            return Response({'failure': "cannot change permissions on this object"},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Try to get the user that the request user is trying to manage permissions on
        try: 
            user = User.objects.get(pk=serializer.validated_data.get("user"))
        except User.DoesNotExist:
            return Response({'failure': AuthError.USER_DOES_NOT_EXIST},
                            status=status.HTTP_400_BAD_REQUEST)

        # Add or change the permission to the request permission
        is_permitted, _ = permission_class.is_permitted_id(
            user_id=user.id,
            obj_id=serializer.validated_data.get(field),
            level=serializer.validated_data.get("level"),
            create=True,
        )

        # If this permission already exists at this level, return a 304
        if is_permitted:
            return Response({'failure': 'user already has this permission'},
                            status=status.HTTP_304_NOT_MODIFIED)
        return Response({'success': 'permissions changed'},
                        status=status.HTTP_200_OK)
