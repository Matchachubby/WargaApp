from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = '__all__'
