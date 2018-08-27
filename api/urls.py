from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views.auth import (
    UserViewSet,
)
from api.views.base import (
    FormViewSet,
    ResponseViewSet,
)

router = DefaultRouter()
router.register(r'forms', FormViewSet, base_name='forms')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'responses', ResponseViewSet, base_name='responses')

urlpatterns = router.urls

