from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm



def pharmacist_list(request):
    medicines = Medicine.objects.all()
    add_form = MedicineForm()
    update_form = MedicineForm()
    context = {
        'medicines': medicines,
        'add_form': add_form,
        'update_form': update_form,
    }
    return render(request, 'pharmacist_list.html', context)

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pharmacist_list')
    return redirect('pharmacist_list')

def update_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('pharmacist_list')
    return redirect('pharmacist_list')

def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('pharmacist_list')
    return redirect('pharmacist_list')
