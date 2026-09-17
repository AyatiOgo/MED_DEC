from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientModel
from .serializers import PatientSerializer
# Create your views here.

class TestView(APIView):
    def get(self, request):

        return Response({
            'data':'This endpoint is seen',
            'status':status.HTTP_200_OK,
            })

class PatientView(APIView):
    def get(self, request, id):
        patient = PatientModel.objects.get(id = id)
        serializer = PatientSerializer(patient)

        return Response(serializer.data, status=status.HTTP_200_OK)