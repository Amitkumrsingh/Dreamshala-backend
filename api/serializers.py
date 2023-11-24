# yourapp/serializers.py

from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'user_type', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_type = validated_data.pop('user_type', 'ST')  # Default to 'ST' (Student) if not provided
        user = CustomUser.objects.create_user(**validated_data, user_type=user_type)
        return user

