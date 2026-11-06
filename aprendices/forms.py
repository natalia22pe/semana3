from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['nombre', 'apellido', 'documento', 'correo', 'telefono', 'ficha', 'programa', 'programa_rel']