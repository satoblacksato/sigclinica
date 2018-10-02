import datetime

from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework import permissions, status, viewsets, views
# Esto se importa para poder traer los turnos de la doctora/o que se logueo
from apps.empleados.models import Empleado
from apps.pacientes.models import Paciente
from apps.pacientes.serializer import PacienteListSerializer

from apps.library.pagination import StandardResultsSetPagination

from .serializer import HistoriaClinicaCreateSerializer
from .models import HistoriaClinica


class HistoriaClinicaViewSet(viewsets.ModelViewSet):

	queryset = HistoriaClinica.objects.all()
	serializer_class = HistoriaClinicaCreateSerializer
	pagination_class = StandardResultsSetPagination

	def get_queryset(self):
		"""
		Se usa para filtrar las fichas clinicas del paciente junto con ese medico
		"""
		queryset = HistoriaClinica.objects.all()
		paciente = self.request.query_params.get('paciente', None)
		empleado = Empleado.objects.filter(usuario__id=self.request.session['id_usuario'])
		if empleado.exists():
			if paciente is not None:
				queryset = queryset.filter(paciente__id=paciente, empleado__id=empleado[0].id)
			return queryset.order_by('-id')

	def create(self, request):
		
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid():
			empleado = Empleado.objects.filter(usuario__id=request.session['id_usuario'])
			if empleado.exists():
				paciente = Paciente.objects.get(pk=serializer.data['paciente'])
				HistoriaClinica.objects.create(motivo_consulta=serializer.data['motivo_consulta'], 
					antecedentes_enfermedad=serializer.data['antecedentes_enfermedad'], 
					diagnostico=serializer.data['diagnostico'], paciente=paciente, empleado=empleado.first(),
					tratamiento=serializer.data['tratamiento'])
				
				return Response(serializer.data)

		return Response({
			'status': 'Bad request',
			'message': 'Account could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)


	#def list(self, request):
	#    pass

	#def create(self, request):
	#    pass

	#def retrieve(self, request, pk=None):
	#    pass

	#def update(self, request, pk=None):
	#    pass

	#def partial_update(self, request, pk=None):
	#    pass

	#def destroy(self, request, pk=None):
	#    pass


class HistoriaClinicaInforme(viewsets.ModelViewSet):

	queryset = HistoriaClinica.objects.all()
	serializer_class = PacienteListSerializer
	pagination_class = StandardResultsSetPagination

	def get_queryset(self):
		"""
		Se usa para filtrar las fichas clinicas del paciente junto con ese medico
		"""
		id_pacientes = []
		queryset = HistoriaClinica.objects.all()
		empleado = Empleado.objects.filter(usuario__id=self.request.session['id_usuario'])
		if empleado.exists():
			queryset = queryset.filter(empleado__id=empleado[0].id)
			for q in queryset:
				id_pacientes.append(q.paciente.id)
			paciente = Paciente.objects.filter(id__in=id_pacientes)
			return paciente