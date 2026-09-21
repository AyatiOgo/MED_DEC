from django.urls import path
from .views import *

urlpatterns = [
    path('test/', TestView.as_view() , name=''),
    path('patient/<int:id>/', PatientView.as_view() , name='patient_view'),
    path('med_prec/<int:id>/', MedicationPrescView.as_view() , name='med_presc_view'),
    path('med_prec/check_med/<int:id>/', MedicationPrescView.as_view() , name='med_check_view'),
]
