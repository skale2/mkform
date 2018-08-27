from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from forms.models.base import (
    Form,
    Response,
)
from api.serializers.base import (
    FormShortSerializer,
    ResponseShortSerializer,
    FormSerializer,
    ResponseSerializer,
)
from api.permissions import (
    CanManagePermission,
    CanEditPermission,
    CanRespondPermission,
    CanViewPermission,
)


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    permission_classes = (CanViewPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return FormShortSerializer
        return FormSerializer

    @action(
        methods=['post', 'patch'],
        detail=True, 
        permission_classes=(CanManagePermission,),
    )
    def transfer_ownership(self, request, pk=None):
        pass

    @action(
        methods=['get'], 
        detail=False,
    )
    def search(self, request):
        pass

    @action(
        methods=['post'],
        detail=True,
        permission_classes=(CanRespondPermission,),
    )
    def respond(self, request, pk=None):
        pass
    
    @action(
        methods=['get'],
        detail=True,
        permission_classes=(CanEditPermission,),
    )
    def responses(self, request, pk=None):
        pass


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    permission_classes = (CanViewPermission,)

