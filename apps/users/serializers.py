from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'passport', 'first_name', 'last_name', 'surname', 'phone_number')
        write_only_fields = ['password']
                                        
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Такая почта уже существует!')
        return email
        
    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'