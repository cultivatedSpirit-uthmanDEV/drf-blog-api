from  account.serializer import RegisterSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError



class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
register_view = RegisterAPIView


def login_out(request):
    try: 
        token = request.data['refresh_token']
        refresh_token = RefreshToken(token)
        refresh_token.blacklist()

        return Response({"message" : "You have been sucessfully logged out"})
    except TokenError:
        return Response({"error" : "Invalid Token"})


