import datetime

from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import TurnoSerializer, TurnoCreateSerializer
from .models import Turno

# Esto se importa para poder traer los turnos de la doctora/o que se logueo
from apps.empleados.models import Empleado


class TurnoViewSet(viewsets.ModelViewSet):

	queryset = Turno.objects.all()
	serializer_class = TurnoCreateSerializer


# Esta clase solo va a traer los turnos que le corresponden a cada doctor al que se logueo
class TurnoDelDia(viewsets.ModelViewSet):

	'''
		Clase que solo trae los pacientes del usuario que se logueo y del dia actual
	'''

	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

	def list(self, request):

		empleado = Empleado.objects.filter(usuario__id=request.session['id_usuario'])
		print(empleado)
		if empleado.exists():
			queryset = Turno.objects.filter(empleado__id=empleado[0].id, fecha=datetime.datetime.today()).order_by('start')
		else:
			queryset = []
		print(queryset)
		serializer = TurnoSerializer(queryset, many=True)
		return Response(serializer.data)
