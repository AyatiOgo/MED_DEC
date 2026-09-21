from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PatientModel, MedicationPrescriptionModel, MedicationModel
from .serializers import PatientSerializer, Medication_Presc_Serializer, MedicationSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .services.image_comp import compare_images
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
    parser_classes = [
        MultiPartParser,
        FormParser,
    ]
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

    def post(self, request, id):

        try:
            patient = PatientModel.objects.get(id = id)

        except PatientModel.DoesNotExist:
            return  Response({
                'error' : 'Patient Does Not Exist',
                'status' : status.HTTP_404_NOT_FOUND,
            })
        try: 
            medication_prec = MedicationPrescriptionModel.objects.get(patient = patient)
        except MedicationPrescriptionModel.DoesNotExist:
             return  Response({
                            'error' : 'Mediction Prescription Does Not Exist',
                            'status' : status.HTTP_404_NOT_FOUND,
                        })
        uploaded_image = request.FILES.get('image')
        patient_image = medication_prec.med_presc_image

        if not uploaded_image:
            return Response({
                'error': 'Not reading uploaded image'
            })

        if not patient_image :
            return Response({
                'error' : 'No Patient Medication Image Uploaded', 
                'status': status.HTTP_404_NOT_FOUND
            })

        temp_path = default_storage.save( f"temp/{uploaded_image.name}",uploaded_image)

        uploaded_image_path = default_storage.path(temp_path)

        try: 
          similiraty_score =   compare_images(uploaded_image_path , patient_image.path)
        except Exception as e :
            return Response({
                'error' : 'An Error Occured'
            })
        
        return Response({
            'similarity' : similiraty_score,
            'status':status.HTTP_200_OK
        })

