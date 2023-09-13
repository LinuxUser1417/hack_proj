from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name="Корзина")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name} in {self.cart.user.username}'s cart"


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"Favorites for {self.user.username}"


class OrderStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус заказа")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name="Заказы")
    status = models.ForeignKey(
        OrderStatus, on_delete=models.CASCADE, verbose_name="История заказов")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(verbose_name="Рейтинг пользователя")

    def __str__(self):
        return f"Rating for {self.user.username}"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='Пользователь')
    street_address = models.CharField(max_length=255, verbose_name='Улица и номер дома')
    city = models.CharField(max_length=100, verbose_name='Город')
    zip_code = models.CharField(max_length=10, verbose_name='Почтовый индекс')
    is_default = models.BooleanField(default=False, verbose_name='Адрес по умолчанию')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'Адрес пользователя {self.user.username}'