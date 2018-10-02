from django.db import models

from apps.pacientes.models import Paciente
from apps.empleados.models import Empleado


class Turno(models.Model):

    estados = (('presente', 'presente'),
              ('cambio', 'cambio'),
              ('atendido', 'atendido'))  

    paciente = models.ForeignKey(Paciente, null=True, blank=True)
    title = models.CharField(max_length=800, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    allDay = models.BooleanField(default=False)
    backgroundColor = models.CharField(max_length=2000, default='#80FF00', null=True, blank=True)

    motivo = models.CharField(max_length=2000, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, null=True, blank=True)
    fecha = models.DateField(auto_now=True, blank=True, null=True)
    hora = models.DateTimeField(auto_now=True, blank=True, null=True)
    estado = models.CharField(max_length=800, choices=estados, null=True, blank=True)
    

    def __str__(self):

    	return '%s' % str(self.paciente)

    class Meta:
    	verbose_name = 'Turno'
    	verbose_name_plural = 'Turnos'
