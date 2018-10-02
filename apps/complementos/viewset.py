from rest_framework import viewsets

from apps.library.pagination import StandardResultsSetPagination
from apps.pacientes.models import ObraSocial

from .serializer import TipoDocumentoSerializer, ObraSocialSerializer
from .models import TipoDocumento


class TipoDocumentoViewSet(viewsets.ModelViewSet):

    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class ObraSocialViewSet(viewsets.ModelViewSet):

	queryset = ObraSocial.objects.all()
	serializer_class = ObraSocialSerializer