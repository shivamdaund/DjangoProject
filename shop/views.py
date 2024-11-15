from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from .forms import PlantForm

# List view
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

# Detail view
def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    return render(request, 'plant_detail.html', {'plant': plant})

# Create view
def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plant_form.html', {'form': form})

# Update view
def plant_update(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plant_form.html', {'form': form})

# Delete view
def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('plant_list')
    return render(request, 'plant_confirm_delete.html', {'plant': plant})
# shop/views.py

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Plant
from .forms import QuantityDeleteForm

def plant_delete(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    
    if request.method == 'POST':
        form = QuantityDeleteForm(request.POST)
        if form.is_valid():
            delete_quantity = form.cleaned_data['quantity']
            
            # Reduce quantity by the specified amount
            plant.quantity -= delete_quantity
            
            if plant.quantity <= 0:
                # Delete the plant if quantity is zero or less
                plant.delete()
            else:
                # Save the updated quantity
                plant.save()
                
            return redirect('plant_list')
    else:
        form = QuantityDeleteForm()

    return render(request, 'plant_confirm_delete.html', {'plant': plant, 'form': form})


