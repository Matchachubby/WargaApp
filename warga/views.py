from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm
from .serializers import WargaSerializer, PengaduanSerializer


# ======================
#   HTML VIEW
# ======================

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
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'object_list'


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


# ======================
#      API VIEWSET
# ======================

# Warga API - publik boleh GET, tapi butuh login untuk POST/PUT/DELETE
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAdminUser]
    
    # Filter & search & ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # fields yang boleh dicari pakai ?search=
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    # fields yang boleh di-order pakai ?ordering=
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']
    # opsional: default ordering jika parameter ordering tidak disertakan
    ordering = ['-tanggal_registrasi']


# Pengaduan API - Hanya admin (is_staff=True) boleh akses
class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]  # jika masih ingin hanya admin
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']
    ordering = ['-tanggal_lapor']



# ======================
#      API VIEWSET
# ======================

#class WargaViewSet(viewsets.ModelViewSet):
    #queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    #serializer_class = WargaSerializer


#class PengaduanViewSet(viewsets.ModelViewSet):
    #queryset = Pengaduan.objects.all().order_by('-tanggal_lapor')
    #serializer_class = PengaduanSerializer

