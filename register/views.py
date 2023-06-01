from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


class UserCreateAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'ok': True }, status=status.HTTP_201_CREATED)
        return Response({'ok': False, 'errors': serializer.errors}, status=status.HTTP_202_ACCEPTED)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'access': str(refresh.access_token),
                    'ok': True,
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': 'Invalid credentials',
                    'ok': False,
                }, 
                status=status.HTTP_204_NO_CONTENT
            )