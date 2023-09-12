from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, PhotoViewSet, VideoViewSet



router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
