from rest_framework import routers
from django.urls import path, include
from .views import TypeViewSet, ProductVideoViewSet, ProductViewSet, ProductImageViewSet, ReviewImageViewSet, ReviewViewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register('favorite', FavoriteViewSet, basename='favorite')
router.register('products/categories', TypeViewSet, basename='type')
router.register('products', ProductViewSet, basename='product')
router.register('shorts', ProductVideoViewSet, basename='short')
router.register('images', ProductImageViewSet, basename='image')
router.register('review', ReviewViewSet, basename='review')
router.register('review/images', ReviewImageViewSet, basename='review-images')

urlpatterns = router.urls