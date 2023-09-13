from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from .models import (Product, ProductImage, ProductVideo, Review, ReviewImage, Favorite,
                     Types)
from .serializers import (ProductImageSerializer, ProductSerializer,
                          ProductVideoSerializer, ReviewImageSerializer,
                          ReviewSerializer, TypeSerializer, FavoriteSerializer)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypeSerializer

    @swagger_auto_schema(operation_summary="Получить список всех типов", operation_description="Эндпоинт для просмотра списка всех доступных типов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый тип", operation_description="Эндпоинт для создания нового типа. Необходимо передать данные нового типа.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного типа", operation_description="Эндпоинт для просмотра деталей выбранного типа.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить тип", operation_description="Эндпоинт для обновления данных типа. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить тип", operation_description="Эндпоинт для частичного обновления данных типа. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить тип", operation_description="Эндпоинт для удаления типа.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    @swagger_auto_schema(operation_summary="Получить список всех продуктов", operation_description="Эндпоинт для просмотра списка всех доступных продуктов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного продукта", operation_description="Эндпоинт для просмотра деталей выбранного продукта.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить продукт", operation_description="Эндпоинт для обновления данных продукта. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить продукт", operation_description="Эндпоинт для частичного обновления данных продукта. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить продукт", operation_description="Эндпоинт для удаления продукта.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый продукт", operation_description="Эндпоинт для создания нового продукта. Необходимо передать данные нового продукта.")
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

    @swagger_auto_schema(operation_summary="Получить список всех изображений продукта", operation_description="Эндпоинт для просмотра списка всех доступных изображений продукта.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новое изображение продукта", operation_description="Эндпоинт для создания нового изображения продукта. Необходимо передать данные нового изображения продукта.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного изображения продукта", operation_description="Эндпоинт для просмотра деталей выбранного изображения продукта.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить изображение продукта", operation_description="Эндпоинт для обновления данных изображения продукта. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить изображение продукта", operation_description="Эндпоинт для частичного обновления данных изображения продукта. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить изображение продукта", operation_description="Эндпоинт для удаления изображения продукта.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ProductVideoViewSet(viewsets.ModelViewSet):
    queryset = ProductVideo.objects.all()
    serializer_class = ProductVideoSerializer

    @swagger_auto_schema(operation_summary="Получить список всех видео продукта", operation_description="Эндпоинт для просмотра списка всех доступных видео продукта.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новое видео продукта", operation_description="Эндпоинт для создания нового видео продукта. Необходимо передать данные нового видео продукта.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного видео продукта", operation_description="Эндпоинт для просмотра деталей выбранного видео продукта.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить видео продукта", operation_description="Эндпоинт для обновления данных видео продукта. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить видео продукта", operation_description="Эндпоинт для частичного обновления данных видео продукта. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить видео продукта", operation_description="Эндпоинт для удаления видео продукта.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @swagger_auto_schema(operation_summary="Получить список всех отзывов", operation_description="Эндпоинт для просмотра списка всех доступных отзывов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый отзыв", operation_description="Эндпоинт для создания нового отзыва. Необходимо передать данные нового отзыва.")
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

    @swagger_auto_schema(operation_summary="Получить детали определенного отзыва", operation_description="Эндпоинт для просмотра деталей выбранного отзыва.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить отзыв", operation_description="Эндпоинт для обновления данных отзыва. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить отзыв", operation_description="Эндпоинт для частичного обновления данных отзыва. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить отзыв", operation_description="Эндпоинт для удаления отзыва.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ReviewImageViewSet(viewsets.ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer

    @swagger_auto_schema(operation_summary="Получить список всех изображений отзывов", operation_description="Эндпоинт для просмотра списка всех доступных изображений отзывов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новое изображение отзыва", operation_description="Эндпоинт для создания нового изображения отзыва. Необходимо передать данные нового изображения отзыва.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного изображения отзыва", operation_description="Эндпоинт для просмотра деталей выбранного изображения отзыва.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить изображение отзыва", operation_description="Эндпоинт для обновления данных изображения отзыва. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить изображение отзыва", operation_description="Эндпоинт для частичного обновления данных изображения отзыва. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить изображение отзыва", operation_description="Эндпоинт для удаления изображения отзыва.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    @swagger_auto_schema(operation_summary="Получить список всех избранных продуктов", operation_description="Эндпоинт для просмотра списка всех избранных продуктов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый избранный продукт", operation_description="Эндпоинт для создания нового избранного продукта. Необходимо передать данные нового избранного продукта.")
    def create(self, request, *args, **kwargs):
        # Передаєм user в context сериализатора
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Получить детали определенного избранного продукта", operation_description="Эндпоинт для просмотра деталей выбранного избранного продукта.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить избранного продукта", operation_description="Эндпоинт для обновления данных избранного продукта. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить избранного продукта", operation_description="Эндпоинт для частичного обновления данных избранного продукта. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить избранного продукта", operation_description="Эндпоинт для удаления избранного продукта.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    @swagger_auto_schema(operation_summary="Получить список избранных продуктов пользователя", operation_description="Эндпоинт для просмотра списка всех избранных продуктов конкретного пользователя.")
    def my_favorites(self, request):
        user = self.request.user
        if not user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        favorites = Favorite.objects.filter(user=user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)