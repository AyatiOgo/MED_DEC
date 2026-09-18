from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientModel, MedicationPrescriptionModel, MedicationModel
from .serializers import PatientSerializer, Medication_Presc_Serializer, MedicationSerializer
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

class MedicationPrescView(APIView):
    def get(self, request, id):

        try:
            patient = PatientModel.objects.get(id = id)

        except PatientModel.DoesNotExist:
            return Response({
                                'error' : 'Patient Does Not Exist',
                                'status' : status.HTTP_404_NOT_FOUND
                             })

        
        medication_presc = MedicationPrescriptionModel.objects.get(patient = patient)
        medications = MedicationModel.objects.filter(prescription = medication_presc)
        serializer_presc = Medication_Presc_Serializer(medication_presc)
        serializer_med = MedicationSerializer(medications, many=True)


        return Response( {
                'prescription':serializer_presc.data,
                'medications': serializer_med.data,
                'status': status.HTTP_200_OK
        })
    