from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, ShopViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('profile', UserViewSet, basename='profile')
router.register('shops', ShopViewSet, basename='shop')
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
            path('', include(router.urls)),
            ]

