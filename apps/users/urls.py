from rest_framework import routers
from django.urls import path, include
from .views import RegisterView, ChangePasswordView, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
            path('', include(router.urls)),
            path('registration/', RegisterView.as_view(), name='register'),
            path('change-password/', ChangePasswordView.as_view(), name='change_password'),
            ]

