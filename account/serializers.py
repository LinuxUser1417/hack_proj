from rest_framework import serializers
from .models import *

class CustomUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserManager
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

