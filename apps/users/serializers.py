from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Shop

User = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('last_login', 'is_superuser', 'is_active', 'is_staff', 'password_reset_code', 'groups', 'user_permissions')
        write_only_fields = ('password')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        read_only_fields = ('id', 'user', 'rating', 'verified')

    def create(self, validated_data):
        user = self.context.get('user')
        shop = Shop.objects.create(user=user, **validated_data)
        return shop