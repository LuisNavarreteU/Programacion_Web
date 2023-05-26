from django import forms
from .models import Libros,Usuario

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = '__all__'

class UsuarioForm():
    class Meta:
        model = Usuario
        fields = '__all__'