from django.db import models
from apps.complementos.models import TipoDocumento


class Persona(models.Model):

    nombre = models.CharField(max_length=600, blank=True, null=True)
    apellido = models.CharField(max_length=600, blank=True, null=True)
    tipo_documento = models.CharField(max_length=800, blank=True, null=True)
    documento = models.CharField(max_length=600, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
