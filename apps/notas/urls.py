from django.conf.urls import url,include
from rest_framework import routers

from .views import NotaTemplateView

from . import viewset


router = routers.DefaultRouter()
router.register(r'notas', viewset.NotaViewSet)


urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^$', NotaTemplateView.as_view(), name='notas-lectura-alta')
]
