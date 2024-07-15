from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'admission_date', 'diagnosis', 'room_number', 'discharge_date']


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'admission_date', 'diagnosis', 'room_number', 'discharge_date']