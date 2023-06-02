from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import QualifySerializer
from .models import Qualify


class ListQualifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qualifications = Qualify.objects.all()
        serializer = QualifySerializer(qualifications, many=True)
        return Response({'ok': True, 'qualifications': serializer.data})


class QualifyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, turn):
        request.data['turn'] = turn
        serializer = QualifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'ok':True }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)