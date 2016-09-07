from django import forms
from .models import Bicicleta


class BicicletaForm(forms.ModelForm):

    class Meta:
        model = Bicicleta
        fields = ('fabricante', 'modelo', 'cor', 'marcha', 'marcaDoCambio', 'dono', 'celular', 'email')
