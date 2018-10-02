from django.conf.urls import url, include
from rest_framework import routers
from . import viewset

from .views import ChatView

router = routers.DefaultRouter()
router.register(r'chat', viewset.MensajeViewSet)
router.register(r'usuarios', viewset.UsuarioViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^sala/$', ChatView.as_view(), name='sala-chat')
]
