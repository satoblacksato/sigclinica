from rest_framework import viewsets

from apps.library.pagination import StandardResultsSetPagination

from .serializer import PacienteCreateSerializer, FotoSerializer, PacienteListSerializer
from .models import Paciente, Foto


class PacienteViewSet(viewsets.ModelViewSet):

    queryset = Paciente.objects.all()
    serializer_class = PacienteCreateSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        '''
            Buscador de pacientes, se encarga de encontrar un paciente por todos sus datos
        '''
        queryset = Paciente.objects.all()
        apellido = self.request.query_params.get('apellido', None)
        nombre = self.request.query_params.get('nombre', None)
        documento = self.request.query_params.get('documento', None)
        obra_social = self.request.query_params.get('obra_social', None)

        if apellido is not None:
            queryset = Paciente.objects.filter(apellido__icontains=apellido)
        if nombre is not None:
            queryset = Paciente.objects.filter(nombre__icontains=nombre)
        if documento is not None:
            queryset = Paciente.objects.filter(documento__icontains=documento)
        if obra_social is not None:
            queryset = Paciente.objects.filter(obra_social__descripcion__icontains=obra_social)       
        return queryset

    def get_serializer_class(self):
    	if self.action == 'list':
    		return PacienteListSerializer
    	else:
    		return PacienteCreateSerializer


class PacienteSelectViewSet(viewsets.ModelViewSet):

    queryset = Paciente.objects.all()
    serializer_class = PacienteCreateSerializer


class FotoViewSet(viewsets.ModelViewSet):

    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
