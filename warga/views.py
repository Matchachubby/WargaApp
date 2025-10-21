from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from .models import Warga, Pengaduan
from django.urls import reverse_lazy
from .forms import WargaForm, PengaduanForm

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'object_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'  
    context_object_name = 'warga'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'  # lokasi template
    context_object_name = 'object_list'  # opsional, default-nya juga 'object_list'

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'  
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')


class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

    
# Create your views here.
