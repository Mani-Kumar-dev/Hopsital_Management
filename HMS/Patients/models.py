from django.db import models

"""
We are generating custom patient id as a primary key
"""

from .gen_pid import generate_id


class BaseModel(models.Model):
    patient_id = models.CharField(primary_key=True, editable=False, max_length=8)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class IssueChoices(models.TextChoices):
    consultation = 'CONSULTATION', 'Consultation'
    surgery = 'SURGERY', 'Surgery'


class PatientRegistration(BaseModel):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=False)
    mobile = models.IntegerField(blank=True, max_length=10)
    country = models.CharField(blank=False, max_length=13)
    state = models.CharField(blank=False, max_length=15)
    city = models.CharField(blank=False, max_length=13)
    address = models.TextField()
    blood_group = models.CharField(max_length=10)
    issue_type = models.CharField(max_length=15, choices=IssueChoices.choices, blank=False)  # consultation/surgery
    previous_medical_history = models.TextField(verbose_name='medical history')

    def save(self, *args, **kwargs):
        if not self.patient_id:
            self.patient_id = generate_id()
        super().save(*args, **kwargs)


class AdmissionDetails(BaseModel):
    admission_reason = models.TextField(verbose_name="Reason For Admission", blank=False)
    admission_date = models.DateField(verbose_name="Date of Admission", editable=True)
    discharge_date = models.DateField(verbose_name="Date of Discharge", blank=True, null=True)
    patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE)
