from django.conf.urls import url,include

from rest_framework import routers

from . import viewset
from .views import HistoriaClinicaView

router = routers.DefaultRouter()
router.register(r'historia_clinica', viewset.HistoriaClinicaViewSet)
router.register(r'historia_informe', viewset.HistoriaClinicaInforme)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^informe/$', HistoriaClinicaView.as_view(), name='informe-historia-clinicas')
]
