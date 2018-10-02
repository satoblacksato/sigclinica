"""sigclinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls)) ALan
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import Dashboard, NoEmpleado

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ingresar, name='ingresar'),
    url(r'^cerrar/$', views.cerrar, name='cerrar-session'),
    url(r'^empleados/', include('apps.empleados.urls')),
    url(r'^turnos/', include('apps.turnos.urls')),
    url(r'^notas/', include('apps.notas.urls')),
    url(r'^chat/', include('apps.chat.urls')),
    url(r'^historia/clinica/', include('apps.historiaclinicas.urls')),
    url(r'^complementos/', include('apps.complementos.urls')),
    url(r'^pacientes/', include('apps.pacientes.urls')),
    url(r'^dashboard/$', Dashboard.as_view(), name='home'),
    url(r'^noempleado/$', NoEmpleado.as_view(), name='no-empleado')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
