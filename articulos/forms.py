from django import forms
from articulos.models import Articulos

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = "__all__"