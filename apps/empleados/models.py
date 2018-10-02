from django.db import models
from django.contrib.auth.models import User

from apps.personas.models import Persona


choices = (
        ('medico', 'Médico'),
        ('secretariado', 'Secretariado'),
        ('programador', 'Programador')
        )


class Empleado(Persona):

    usuario = models.OneToOneField(User, blank=False, null=False)
    foto = models.ImageField(upload_to='fotos_empleados', blank=True, null=True)
    categoria = models.CharField(choices=choices, max_length=800, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
