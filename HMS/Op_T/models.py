

# Create your models here.
# operation_theatre/models.py
from django.db import models

class OperationTheatre(models.Model):
    patient_ID = models.IntegerField()
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Disease = models.CharField(max_length=100)
    Type_of_Surgery = models.CharField(max_length=100)
    Surgery_Doctors = models.CharField(max_length=255)
    Surgery_Nurses = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.Name
