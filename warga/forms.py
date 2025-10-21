from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = '__all__'


class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = '__all__'
