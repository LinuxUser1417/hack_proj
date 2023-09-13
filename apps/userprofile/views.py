from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from drf_yasg.utils import swagger_auto_schema
from .serializers import CartSerializer, CartItemSerializer, FavoritesSerializer, OrderStatusSerializer, OrderSerializer, RatingSerializer, AddressSerializer
from .models import UserProfile, Cart, CartItem, Favorites, OrderStatus, Order, Rating, Address
from rest_framework.decorators import action
from rest_framework.response import Response

@swagger_auto_schema(operation_summary="Получить список данных пользователя", operation_description="Эндпоинт для просмотра списка данных пользователя.")
class UserProfileListView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk=None):
        user_profile = self.get_object()
        # Ваш код для выполнения дополнительного действия
        return Response({"message": "Вы выполнили дополнительное действие для пользователя с ID {}".format(pk)})



@swagger_auto_schema(operation_summary="Получить данные пользователя по ID", operation_description="Эндпоинт для просмотра данных пользователя по ID.")
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


@swagger_auto_schema(operation_summary="Получить список корзин", operation_description="Эндпоинт для просмотра списка корзин.")
class CartListView(viewsets.ViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request):
        carts = Cart.objects.all()
        serializer = self.serializer_class(carts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk=None):
        try:
            cart = Cart.objects.get(pk=pk)
            return Response({"message": "Вы выполнили дополнительное действие для корзины с ID {}".format(pk)})
        except Cart.DoesNotExist:
            return Response({"error": "Корзина с указанным ID не найдена"}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(operation_summary="Получить корзину по ID", operation_description="Эндпоинт для просмотра корзины по ID.")
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


@swagger_auto_schema(operation_summary="Получить список избранных элементов", operation_description="Эндпоинт для просмотра списка избранных элементов.")
class FavoriteListView(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk=None):
        favorite = self.get_object()
        return Response({"message": "Вы выполнили дополнительное действие для избранного элемента с ID {}".format(pk)})


@swagger_auto_schema(operation_summary="Получить избранный элемент по ID", operation_description="Эндпоинт для просмотра избранного элемента по ID.")
class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer


@swagger_auto_schema(operation_summary="Получить список истории заказов", operation_description="Эндпоинт для просмотра списка истории заказов.")
class OrderHistoryViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk=None):
        order_status = self.get_object()
        return Response({"message": "Вы выполнили дополнительное действие для статуса заказа с ID {}".format(pk)})


@swagger_auto_schema(operation_summary="Получить запись истории заказа по ID", operation_description="Эндпоинт для просмотра записи истории заказа по ID.")
class OrderHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


@swagger_auto_schema(operation_summary="Получить список статусов товаров", operation_description="Эндпоинт для просмотра списка статусов товаров.")
class OrderListView(viewsets.ViewSet):
    queryset = Order.objects.all()  
    serializer_class = OrderSerializer  
    def list(self, request):
    
        orders = self.queryset
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['GET'])
    def extra_action(self, request, pk=None):
        try:
            order = self.queryset.get(pk=pk)
            # Выполняйте здесь ваше дополнительное действие
            message = f"Вы выполнили дополнительное действие для заказа с ID {pk}"
            return Response({"message": message})
        except Order.DoesNotExist:
            return Response({"message": "Заказ не найден"}, status=404)


@swagger_auto_schema(operation_summary="Получить статус товара по ID", operation_description="Эндпоинт для просмотра статуса товара по ID.")
class ProductStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserRatingListView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


@swagger_auto_schema(operation_summary="Получить рейтинг пользователя по ID", operation_description="Эндпоинт для просмотра рейтинга пользователя по ID.")
class UserRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


@swagger_auto_schema(operation_summary="Получить список адресов пользователей", operation_description="Эндпоинт для просмотра списка адресов пользователей.")
class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@swagger_auto_schema(operation_summary="Получить адрес пользователя по ID", operation_description="Эндпоинт для просмотра адреса пользователя по ID.")
class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@swagger_auto_schema(operation_summary="Получить список адресов пользователей",
                     operation_description="Эндпоинт для просмотра списка адресов пользователей.")
class AddressListView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


@swagger_auto_schema(operation_summary="Получить список элементов корзины",
                     operation_description="Эндпоинт для просмотра списка элементов корзины.")
class CartItemListView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


@swagger_auto_schema(operation_summary="Получить элемент корзины по ID",
                     operation_description="Эндпоинт для просмотра элемента корзины по ID.")
class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
