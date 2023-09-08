from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, PasswordChangeSerializer, UsersSerializer

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = self.request.user
        serializer = UsersSerializer(user)
        return Response(serializer.data)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'User registered successfully.'})


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    @swagger_auto_schema(request_body=PasswordChangeSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            
            try:
                # Получаем текущего пользователя из базы данных
                user = User.objects.get(username=request.user.username)
            except User.DoesNotExist:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            
            # Проверяем, соответствует ли предоставленный пароль текущему паролю в базе данных
            if not user.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            # Если пароль верный, устанавливаем новый пароль
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






