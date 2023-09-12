from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ShopViewSet, CustomUserViewSet, CustomTokenVerifyView, CustomTokenObtainPairView, CustomTokenRefreshView

router = routers.DefaultRouter()
router.register('shops', ShopViewSet, basename='shop')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
            path('', include(router.urls)),
            path('auth/users/<int:pk>/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
            path('auth/users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
            path('auth/users/activation/', CustomUserViewSet.as_view({'post': 'activation'}), name='user-activation'),
            path('auth/users/resend_activation/', CustomUserViewSet.as_view({'post': 'resend_activation'}), name='user-resend-activation'),
            path('auth/users/set_password/', CustomUserViewSet.as_view({'post': 'set_password'}), name='user-set-password'),
            path('auth/users/reset_password/', CustomUserViewSet.as_view({'post': 'reset_password'}), name='user-reset-password'),
            path('auth/users/reset_password_confirm/', CustomUserViewSet.as_view({'post': 'reset_password_confirm'}), name='user-reset-password-confirm'),
            path('auth/users/set_username/', CustomUserViewSet.as_view({'post': 'set_username'}), name='user-set-username'),
            path('auth/users/reset_username/', CustomUserViewSet.as_view({'post': 'reset_username'}), name='user-reset-username'),
            path('auth/users/reset_username_confirm/', CustomUserViewSet.as_view({'post': 'reset_username_confirm'}), name='user-reset-username-confirm'),
            path('auth/users/me/', CustomUserViewSet.as_view({'get': 'me', 'put': 'me', 'patch': 'me', 'delete': 'me'}), name='user-me'),
            
            
            path('auth/jwt/create/', CustomTokenObtainPairView.as_view(), name="jwt-create"),
            path('auth/jwt/refresh/', CustomTokenRefreshView.as_view(), name="jwt-refresh"),
            path('auth/jwt/verify/', CustomTokenVerifyView.as_view(), name="jwt-verify"),
            ]

