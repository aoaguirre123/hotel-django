from django import forms
from .models import Servicio, Promocion
from django.forms.widgets import DateInput
from django.core.validators import MinValueValidator, MaxValueValidator



class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
        widgets = {
            'tipo_servicio': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control fw-semibold'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'porcentaje_descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    porcentaje_descuento = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )