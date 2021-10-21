from shop.serializers.user_serializer import UserSerializer
from  rest_framework import generics
from django.contrib.auth import get_user_model
from config.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework import viewsets

class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
 
class UsersViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer    