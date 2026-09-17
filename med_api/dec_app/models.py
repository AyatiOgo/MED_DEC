from django.db import models

# Create your models here.

class PatientModel(models.Model):
    first_name = models.CharField(max_length= 100 )
    last_name = models.CharField(max_length=100)
    condition = models.CharField(max_length=1000)
    med_image = models.ImageField(upload_to='media')

    def __str__(self):
        return f' {self.id}|{self.first_name}'