

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class CustomerUserCreate(APIView):
    Permission_classes = [AllowAny]
    
    def post(self, request): 
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            newuser = register_serializer.save()
            if newuser: 
                return Response(status=status.HTTP_200_OK)
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BlackListTokenView(APIView):
    permissions =[AllowAny]
    
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)