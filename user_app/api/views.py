from user_app.api.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from user_app import models

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework.views import APIView

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
       
        else:
            return serializer.errors
            
        return Response(token)

class LogoutView(APIView):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)