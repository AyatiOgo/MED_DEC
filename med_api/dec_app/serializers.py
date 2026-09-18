from rest_framework import serializers
from .models import PatientModel, MedicationPrescriptionModel, MedicationModel

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientModel
        fields = '__all__'


class Medication_Presc_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationPrescriptionModel
        fields = ['med_presc_image']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationModel
        fields = ['name', 'grams', 'amount']