from django import forms
from apps.cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields={
            'id',
            'tipo',
            'placa',
            'color',
            'fecha_in',
            'fecha_out',
            'owner',
        }
        widgets={
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'tipo':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'placa':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'color':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'fecha_in':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'fecha_out':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }
