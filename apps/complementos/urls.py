from django.conf.urls import url,include
from rest_framework import routers

from .views import TipoDocumentoTemplateView, ObraSocialTemplateView

from . import viewset

router = routers.DefaultRouter()
router.register(r'tipodocumento', viewset.TipoDocumentoViewSet)
router.register(r'obrasocial', viewset.ObraSocialViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^tipo/documento/$', TipoDocumentoTemplateView.as_view(), name='tipo-documento-alta'),
    url(r'^obra/social/$', ObraSocialTemplateView.as_view(), name='obra-social-alta')
]
