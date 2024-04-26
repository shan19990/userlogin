from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
import jwt

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        payload = {"user_id":user.id,"username":username}
        key='super-secret'
        token = jwt.encode(payload, key)
        attrs['tokens'] = token
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
