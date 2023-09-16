from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


from djoser.views import UserViewSet as DjoserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    

@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Успешный вход!"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Неверные учетные данные."}, status=status.HTTP_400_BAD_REQUEST)
    

    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UsersSerializer

    @swagger_auto_schema(request_body=UsersSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(operation_summary="Получить список всех категорий", operation_description="Эндпоинт для просмотра списка всех доступных категорий.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новую категорию", operation_description="Эндпоинт для создания новой категории. Необходимо передать данные новой категории.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенной категории", operation_description="Эндпоинт для просмотра деталей выбранной категории.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить категорию", operation_description="Эндпоинт для обновления данных категории. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить категорию", operation_description="Эндпоинт для частичного обновления данных категории. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить категорию", operation_description="Эндпоинт для удаления категории.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @swagger_auto_schema(operation_summary="Зарегистрировать новый магазин", operation_description="Эндпоинт для регистрации нового магазина. Необходимо передать токен пользователя и данные нового магазина.")
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def register_shop(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        # Передаём user в context сериализатора
        serializer = self.get_serializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @swagger_auto_schema(operation_summary="Получить список всех магазинов", operation_description="Эндпоинт для просмотра списка всех магазинов.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Создать новый магазин", operation_description="Эндпоинт для создания нового магазина. Необходимо передать данные нового магазина.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Получить детали определенного магазина", operation_description="Эндпоинт для просмотра деталей выбранного магазина.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Обновить информацию о магазине", operation_description="Эндпоинт для обновления данных магазина. Необходимо передать обновленные данные.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Частично обновить информацию о магазине", operation_description="Эндпоинт для частичного обновления данных магазина. Необходимо передать данные для обновления.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Удалить магазин", operation_description="Эндпоинт для удаления магазина.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary='Авторизация',
        operation_description='Эндпоинт для получения access и refresh токена'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary='JWT Refresh',
        operation_description='This endpoint is used for refreshing JWT token'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        operation_summary='JWT Verify',
        operation_description='This endpoint is used for verifying JWT token'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class CustomUserViewSet(DjoserViewSet):
    @swagger_auto_schema(operation_summary='Получить всех пользователей', operation_description="""Эндпоинт для получения всех""")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Мой аккаунт', operation_description="This endpoints is used for edit user's account")
    def me(self, request, *args, **kwargs):
        return super().me(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Регистрация пользователей', operation_description='This endpoint is used for creating a new user')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Получение пользователя по id', operation_description='This endpoint is used for retrieve get a user')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Обновить пользователя', operation_description='This endpoint is used for updating user details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Обновить пользователя партийно', operation_description='This endpoint is used for partial updating user details')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Удалить пользователя', operation_description='This endpoint is used for deleting a user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Активировать аккаунт', operation_description='This endpoint is used for activating a user')
    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        return super().activation(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_summary='Resend Activation', operation_description='This endpoint is used for resending activation to a user')
    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        return super().resend_activation(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Сменить пароль', operation_description='This endpoint is used for setting user password')
    @action(["post"], detail=False)
    def set_password(self, request, *args, **kwargs):
        return super().set_password(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Восстановить пароль', operation_description='This endpoint is used for resetting user password')
    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        return super().reset_password(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Восстановить пароль (Confirm)', operation_description='This endpoint is used for confirming password reset')
    @action(["post"], detail=False)
    def reset_password_confirm(self, request, *args, **kwargs):
        return super().reset_password_confirm(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Сменить username', operation_description='This endpoint is used for setting username')
    @action(["post"], detail=False, url_path=f"set_{User.USERNAME_FIELD}")
    def set_username(self, request, *args, **kwargs):
        return super().set_username(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Восстановить username', operation_description='This endpoint is used for resetting username')
    @action(["post"], detail=False, url_path=f"reset_{User.USERNAME_FIELD}")
    def reset_username(self, request, *args, **kwargs):
        return super().reset_username(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary='Восстановить username (Confirm)', operation_description='This endpoint is used for confirming username reset')
    @action(["post"], detail=False, url_path=f"reset_{User.USERNAME_FIELD}_confirm")
    def reset_username_confirm(self, request, *args, **kwargs):
        return super().reset_username_confirm(request, *args, **kwargs)

    