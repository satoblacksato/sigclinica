from django.conf.urls import url, include
from rest_framework import routers

from .views import PerfilNuevo

from . import viewset

router = routers.DefaultRouter()
router.register(r'empleados', viewset.EmpleadoViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^perfil/alta/$', PerfilNuevo.as_view(), name='perfil-alta')
]
