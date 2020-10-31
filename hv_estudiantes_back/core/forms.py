from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import Usuario


class SignUpForm(UserCreationForm):
    documento = forms.CharField(max_length=15, )
    nombre = forms.CharField(max_length=70)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=13, required=False, help_text='Opcional')
    direccion = forms.CharField(max_length=50, required=False, help_text='Opcional')
    fecha_nacimiento = forms.DateField(required=False, help_text='Opcional')
    sexo = forms.CharField(max_length=10, required=False, help_text='Opcional')
    nacionalidad = forms.CharField(max_length=30, required=False, help_text='Opcional')
    tipo = forms.CharField(max_length=15, required=False, help_text='Opcional')
    categoria = forms.CharField(max_length=15, required=False, help_text='Opcional')

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'documento', 'nombre', 'email', 'telefono', 'direccion',
                  'fecha_nacimiento', 'sexo', 'nacionalidad', 'tipo', 'categoria')

class SignUpOfferForm(UserCreationForm):
    documento = forms.CharField(max_length=15, )
    nombre = forms.CharField(max_length=70)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=13, required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'documento', 'nombre', 'email', 'telefono')
