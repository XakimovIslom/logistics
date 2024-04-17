from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import LoginSerializer

User = get_user_model()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
