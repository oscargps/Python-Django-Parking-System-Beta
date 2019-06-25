from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.cars.forms import CarForm
from apps.cars.models import Car
# Create your views here.
def Cars_list(request):
    car=Car.objects.all().order_by('id')
    contexto = {'cars':car}
    return render(request, 'cars/index.html', contexto)

def new_car(request):
    
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('index')
    else:
        form=CarForm()
    return render(request, 'cars/cars_form.html',{'form':form})


    