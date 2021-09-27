from shop.serializers.user_serializer import UserSerializer
from  rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

class UserCreate(generics.CreateAPIView):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )