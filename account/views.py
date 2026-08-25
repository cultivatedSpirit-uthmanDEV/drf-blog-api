from  account.serializer import RegisterSerializer
from rest_framework import generics


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
register_view = RegisterAPIView