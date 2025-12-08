from django.urls import path, include
from .views import WargaViewSet, PengaduanViewSet #PengaduanListAPIView, PengaduanDetailAPIView 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'warga', WargaViewSet)
router.register(r'pengaduan', PengaduanViewSet)

urlpatterns = [
    #path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    #path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    #path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(), name='api-pengaduan-detail'),
    path('', include(router.urls)),

]
