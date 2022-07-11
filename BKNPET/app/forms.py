from django import forms
from .models import Producto, Mascota
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
    pass


# ------------------------------------------------------
# APP NUEVA}

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = '__all__'
        