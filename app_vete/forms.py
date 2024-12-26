from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class MascotasFormulario(forms.Form):
    especie = forms.ChoiceField(choices=[
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('pez', 'Pez'),
        ('ave', 'Ave'),
        ('reptil', 'Reptil'),
    ], label="Especie")
    raza = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Raza',
        })
    )
    edad = forms.IntegerField(
        label = '',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Edad',
        })
    )

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
        })
    )
    telefono = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Telefono',
        })
    )
    email = forms.EmailField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        })
    )

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre del producto',
        })
    )
    precio = forms.FloatField(
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Precio del producto',
        })
    )
    categoria = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Categoría',
        })
    )
    descripcion = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Descripción del producto (opcional)',
        }),
        max_length=500,
        required=False,
    )

class SucursalFormulario(forms.Form):
    nombre = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de la sucursal',
        })
    )
    direccion = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Direccion',
        })
    )
    telefono = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Telefono',
        })
    )

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
            }),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }

class PerfilUsuarioForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ["imagen"]




