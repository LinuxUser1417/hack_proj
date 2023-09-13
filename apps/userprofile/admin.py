from django.contrib import admin
from .models import UserProfile, Cart, CartItem, Rating, Favorites, Order, OrderStatus, Address

admin.site.register([UserProfile, Cart, CartItem, Rating, Favorites, Order, OrderStatus, Address])