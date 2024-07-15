from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    admission_date = models.DateField()
    diagnosis = models.TextField()
    room_number = models.IntegerField()
    discharge_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
