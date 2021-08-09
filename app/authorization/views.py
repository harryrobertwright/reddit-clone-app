from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import RegisterSerializer


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
