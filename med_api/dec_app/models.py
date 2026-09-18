from django.db import models

# Create your models here.

class PatientModel(models.Model):
    first_name = models.CharField(max_length= 100 )
    last_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f' {self.id}|{self.first_name}'

GRAM_CHOICES = (
    ('50', 50),
    ('100', 100),
    ('150', 150),
    ('200', 200),
    ('250', 200),
    ('300', 300),
    ('350', 350),
    ('400', 400),
)

class MedicationPrescriptionModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE, related_name='patient')
    med_presc_image = models.ImageField(upload_to='media')

    def __str__(self):
        return f'{self.patient.last_name} | presc'

class MedicationModel(models.Model):
    prescription = models.ForeignKey(MedicationPrescriptionModel, on_delete=models.CASCADE, related_name='prescription')
    name = models.CharField(max_length=200)
    grams = models.CharField(choices=GRAM_CHOICES, max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.prescription.patient.last_name}| med | {self.id}'