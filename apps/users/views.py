from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from apps.users.models import Category, Shop
from .serializers import CategorySerializer, ShopSerializer, UsersSerializer

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = self.request.user
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def register_shop(self, request):
        user = self.request.user
        serializer = ShopSerializer(data=request.data)
        
        if serializer.is_valid():
            # Сохраните магазин с текущим пользователем
            shop = serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)