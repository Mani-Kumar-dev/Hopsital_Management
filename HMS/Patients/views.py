from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, AdmissionForm


def patient_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid. Redirecting to dashboard.")
            form.save()
            print("Form is saved. Redirecting to dashboard.")
            return redirect('patient_dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'base_patients.html', context={'form': form})


def patientDashboard(request):
    return render(request, 'Patient_dashboard.html')


def patient_admission(request):

    if request.method == 'POST':
        form = AdmissionForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("<h4>Admission Success!</h4>")
            # return redirect('patientAdmission')
    else:
        form = AdmissionForm()
    return render(request, 'patient_admission.html', context={'form': form})
