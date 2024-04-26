from django.shortcuts import render
from .serializers import LoginSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data['tokens']
            return Response({'tokens': tokens, 'message': 'Login successful'}, status=200)
        return Response({'message': 'Invalid credentials'}, status=400)
