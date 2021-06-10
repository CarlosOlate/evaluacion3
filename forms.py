from django import forms
from .models import *
from django.forms import ModelForm

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields= '__all__'

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields= '__all__'