from django.shortcuts import render, redirect, get_object_or_404
from .models import LabTest
from .forms import LabTestForm


def add_lab_test(request):
    if request.method == 'POST':
        form = LabTestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    return redirect('labtest_list')

def update_lab_test(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabTestForm(request.POST, request.FILES, instance=lab_test)
        if form.is_valid():
            form.save()
            return redirect('labtest_list')
    return redirect('labtest_list')

def delete_lab_test(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        lab_test.delete()
        return redirect('labtest_list')
    return redirect('labtest_list')

def labtest_list(request):
    lab_tests = LabTest.objects.all()
    return render(request, 'labtest_list.html', {'lab_tests': lab_tests})
