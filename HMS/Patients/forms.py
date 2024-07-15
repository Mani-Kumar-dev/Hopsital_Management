from django import forms
from .models import PatientRegistration, AdmissionDetails


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=PatientRegistration
        exclude = ['patient_id', 'registration_date']
        widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                    'mobile': forms.TextInput(attrs={'class': 'form-control'}),
                    'country': forms.TextInput(attrs={'class': 'form-control'}),
                    'state': forms.TextInput(attrs={'class': 'form-control'}),
                    'city': forms.TextInput(attrs={'class': 'form-control'}),
                    'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                    'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
                    'issue_type': forms.Select(attrs={'class': 'form-control'}),
                    'previous_medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                }


class PatientModelChoice(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.patient_id} :- {obj.first_name} {obj.last_name}'


class AdmissionForm(forms.ModelForm):
    patient = PatientModelChoice(
        queryset=PatientRegistration.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = AdmissionDetails
        fields = "__all__"
        widgets = {
            'admission_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discharge_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
