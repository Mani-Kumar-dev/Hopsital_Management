# operation_theatre/forms.py
from django import forms
from .models import OperationTheatre

class OperationTheatreForm(forms.ModelForm):
    class Meta:
        model = OperationTheatre
        fields = '__all__'
