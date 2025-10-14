from django.urls import path, include
from .views import WargaListView, WargaDetailView 
from .views import PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
]
