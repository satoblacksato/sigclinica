from django.conf.urls import url,include

from rest_framework import routers

from .views import TurnoView, TurnoList, TurnoEspontaneo

from . import viewset

router = routers.DefaultRouter()
router.register(r'turnos', viewset.TurnoViewSet)
router.register(r'turnos-actuales', viewset.TurnoDelDia)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^alta/$', TurnoView.as_view(), name='turnos-alta'),
    url(r'^espontaneo/$', TurnoEspontaneo.as_view(), name='turnos-espontaneo'),
    url(r'^listado/$', TurnoList.as_view(), name='turnos-listado')
]
