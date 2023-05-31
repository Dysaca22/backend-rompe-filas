from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import TurnSerializer
from .models import Turn


class UserTurn(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        turns = Turn.objects.filter(user=user)
        serializer = TurnSerializer(turns, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        serializer = TurnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'ok':True }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)