from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm, PatientUpdateForm

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request):
    patient = Patient.objects.all()
    return render(request, 'patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            print(patient)
            return redirect('patient_list')  # Use the URL name for redirecting
    else:
        form = PatientForm()
    return render(request, 'patient_create.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientUpdateForm(instance=patient)
    return render(request, 'patient_update.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_delete.html', {'patient': patient})
