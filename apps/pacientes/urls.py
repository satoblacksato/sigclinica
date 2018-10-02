from django.conf.urls import url,include
from rest_framework import routers

from .views import PacienteTemplateView

from . import viewset

router = routers.DefaultRouter()
router.register(r'pacientes', viewset.PacienteViewSet)
router.register(r'select', viewset.PacienteSelectViewSet)
router.register(r'fotos', viewset.FotoViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^alta/$', PacienteTemplateView.as_view(), name='paciente-alta')
]
