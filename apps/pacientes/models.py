from django.db import models
from apps.personas.models import Persona
from apps.empleados.models import Empleado


class ObraSocial(models.Model):

    descripcion = models.CharField(max_length=800, null=False, blank=False)

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        verbose_name = 'Obra Social'
        verbose_name_plural = 'Obras Sociales'


class Paciente(Persona):

    foto = models.CharField(max_length=1000, blank=True, null=True)
    tipo_telefono = models.CharField(max_length=1000, blank=True, null=True)
    telefono_celular = models.CharField(max_length=1000, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=1000, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    observacion = models.TextField(max_length=1500, blank=True, null=True)

    # Carnet de afiliado de la obra social
    numero_afiliado = models.CharField(max_length=1000, null=True, blank=True)

    # relacionado con la obra social
    obra_social = models.ForeignKey(ObraSocial, null=True, blank=True)

    edad = models.CharField(max_length=800, null=True, blank=True)

    # domicilio del paciente 
    domicilio = models.CharField(max_length=800, null=True, blank=True)
    
    # relacionado con el medico 
    # empleado = models.ManyToManyField(Empleado, blank=True)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Foto(models.Model):

    #paciente = models.OneToOneField(Paciente, blank=True, null=True)
    file = models.ImageField(upload_to='portadas_libros', blank=True, null=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
