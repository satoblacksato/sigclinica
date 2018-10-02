from rest_framework import serializers

from .models import Turno
from apps.pacientes.serializer import PacienteListSerializer

    #paciente = models.ForeignKey(Paciente, null=True, blank=True)
    #title = models.CharField(max_length=800, null=True, blank=True)
    #start = models.DateTimeField(null=True, blank=True)
    #end = models.DateTimeField(null=True, blank=True)
    #allDay = models.BooleanField(default=False)
    #backgroundColor = models.CharField(max_length=2000, default='#80FF00', null=True, blank=True)

    #motivo = models.CharField(max_length=2000, null=True, blank=True)
    #empleado = models.ForeignKey(Empleado, null=True, blank=True)
    #fecha = models.DateField(auto_now=True, blank=True, null=True)
    #hora = models.DateTimeField(auto_now=True, blank=True, null=True)
    #estado = models.CharField(max_length=800, choices=estados, null=True, blank=True)


class TurnoSerializer(serializers.ModelSerializer):

	paciente = PacienteListSerializer()

	class Meta:
		model = Turno
		fields = '__all__'


class TurnoCreateSerializer(serializers.ModelSerializer):


	class Meta:
		model = Turno
		fields = '__all__'
