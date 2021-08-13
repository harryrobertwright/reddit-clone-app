from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    LoginSerializer, LoginRefreshSerializer, RegisterSerializer
)    


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "User successfully registered.",
            }
        )


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        refresh_token = serializer.validated_data["refresh"]

        del serializer.validated_data["refresh"]

        response = Response(
            serializer.validated_data, status=status.HTTP_200_OK
        )

        response.set_cookie(key="refresh", value=refresh_token, httponly=True)

        return response


class LoginRefreshView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginRefreshSerializer

    def get(self, request):
        serializer = self.get_serializer(data=request.COOKIES)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(
            serializer.validated_data, status=status.HTTP_200_OK
        )

        return response
