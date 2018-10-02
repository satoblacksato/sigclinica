from django.db import models

from apps.pacientes.models import Paciente
from apps.empleados.models import Empleado


class HistoriaClinica(models.Model):

	fecha = models.DateField(auto_now=True)
	hora = models.DateTimeField(auto_now=True)
	paciente = models.ForeignKey(Paciente, null=True, blank=True)
	empleado = models.ForeignKey(Empleado, null=True, blank=True)
	motivo_consulta = models.TextField(max_length=9200, null=True, blank=True)
	antecedentes_enfermedad = models.TextField(max_length=9200, null=True, blank=True)
	diagnostico = models.TextField(max_length=9200, null=True, blank=True)
	tratamiento = models.TextField(max_length=9200, null=True, blank=True)

	def __str__(self):
		return '%s' % str(self.paciente)

	class Meta:
		verbose_name = 'Historia Clínica'
		verbose_name_plural = 'Historias Clínicas'
