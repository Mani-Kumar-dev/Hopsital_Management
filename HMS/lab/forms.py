from django import forms
from .models import LabTest

class LabTestForm(forms.ModelForm):
    TEST_TYPE_CHOICES = [
        ('', 'Choose a Test'),
        ('blood-tests', 'Blood Tests'),
        ('urine-tests', 'Urine Tests'),
        ('stool-tests', 'Stool Tests'),
        ('x-rays', 'X-rays'),
        ('ct-scan', 'CT Scan'),
        ('mri', 'MRI'),
        ('ecg-ekg', 'ECG / EKG'),
        ('endoscopy', 'Endoscopy'),
        ('biopsy', 'Biopsy'),
        ('mammography', 'Mammography'),
        ('pap-smear', 'Pap Smear'),
        ('colonoscopy', 'Colonoscopy'),
        ('pulmonary-tests', 'Pulmonary Function Tests'),
        ('stress-tests', 'Stress Tests'),
        ('cgm', 'Continuous Glucose Monitoring (CGM)'),
        ('holter-monitor', 'Holter Monitor')
    ]
    
    test_type = forms.ChoiceField(choices=TEST_TYPE_CHOICES, required=True)
    
    class Meta:
        model = LabTest
        fields = ['patient_id', 'patient_name', 'patient_age', 'patient_disease', 'test_type', 'test_date', 'technician_name']
