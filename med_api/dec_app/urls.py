from django.urls import path
from .views import *

urlpatterns = [
    path('test/', TestView.as_view() , name=''),
    path('patient/<int:id>/', PatientView.as_view() , name='patient_view'),
]
