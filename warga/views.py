from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga
from .models import Pengaduan

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'  
    context_object_name = 'warga'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'  # lokasi template
    context_object_name = 'object_list'  # opsional, default-nya juga 'object_list'
    
# Create your views here.
