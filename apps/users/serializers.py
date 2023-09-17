from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Shop

User = get_user_model()

from django.contrib.auth.hashers import make_password

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # fields = '__all__'
        read_only_fields = ('rating',)
        exclude = ('last_login', 'is_superuser', 'is_active', 'is_staff', 'password_reset_code', 'groups', 'user_permissions', 'banned', 'total_rating', 'rating_votes',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
class SetRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField()

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Неверное значение рейтинга. Выберите значение от 1 до 5.")
        return value

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