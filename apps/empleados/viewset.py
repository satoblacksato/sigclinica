from rest_framework import viewsets

from apps.library.pagination import StandardResultsSetPagination

from .serializer import EmpleadoCreateSerializer
from .models import Empleado


class EmpleadoViewSet(viewsets.ModelViewSet):

    queryset = Empleado.objects.all()
    serializer_class = EmpleadoCreateSerializer

    def get_queryset(self):
        """
         para traer solos medicos cargados en el sistema
        """
        queryset = Empleado.objects.all()
        categoria = self.request.query_params.get('categoria', None)
        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)
        return queryset
