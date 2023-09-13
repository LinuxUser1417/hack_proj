from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import (Product, ProductImage, ProductVideo, Review, ReviewImage,
                     Types)
from .serializers import (ProductImageSerializer, ProductSerializer,
                          ProductVideoSerializer, ReviewImageSerializer,
                          ReviewSerializer, TypeSerializer)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        # Проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        # Передаём user в context сериализатора
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductVideoViewSet(viewsets.ModelViewSet):
    queryset = ProductVideo.objects.all()
    serializer_class = ProductVideoSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewImageViewSet(viewsets.ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer
