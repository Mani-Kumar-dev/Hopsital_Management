
# operation_theatre/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import OperationTheatre
from .forms import OperationTheatreForm

def list_operation_theatre(request):
    operations = OperationTheatre.objects.all()
    return render(request, 'list.html', {'operations': operations})

def add_operation_theatre(request):
    if request.method == 'POST':
        form = OperationTheatreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = OperationTheatreForm()
    return render(request, 'add.html', {'form': form})

def edit_operation_theatre(request, pk):
    operation = get_object_or_404(OperationTheatre, pk=pk)
    if request.method == 'POST':
        form = OperationTheatreForm(request.POST, instance=operation)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = OperationTheatreForm(instance=operation)
    return render(request, 'edit.html', {'form': form, 'operation': operation})

def delete_operation_theatre(request, pk):
    operation = get_object_or_404(OperationTheatre, pk=pk)
    if request.method == 'POST':
        operation.delete()
        return redirect('list')
    return render(request, 'delete.html', {'operation': operation})
