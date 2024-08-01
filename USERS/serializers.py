from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Poste

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'poste']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password1']
        )
        return user

class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = ['poste']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserLogoutSerializer(serializers.Serializer):
    pass
