from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Warga

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'  
    context_object_name = 'warga'
# Create your views here.
