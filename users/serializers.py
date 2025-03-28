from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'phone_number', 'created_at')


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
