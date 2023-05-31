from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import QualifySerializer
from .models import Qualify


class QualifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, turn):
        qualifications = Qualify.objects.filter(turn_id=turn)
        serializer = QualifySerializer(qualifications, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QualifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'ok':True }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)