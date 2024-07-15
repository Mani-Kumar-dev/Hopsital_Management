from django.db import models

class LabTest(models.Model):
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_disease = models.CharField(max_length=100)
    test_type = models.CharField(max_length=100)
    test_date = models.DateField()
    technician_name = models.CharField(max_length=100)  # New field for lab technician name

    def __str__(self):
        return self.patient_name
