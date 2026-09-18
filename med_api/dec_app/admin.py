from django.contrib import admin
from .models import PatientModel, MedicationPrescriptionModel, MedicationModel
# Register your models here.


admin.site.register(PatientModel)
admin.site.register(MedicationModel)
admin.site.register(MedicationPrescriptionModel)