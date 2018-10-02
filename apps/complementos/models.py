from django.db import models


class TipoDocumento(models.Model):

    descripcion = models.CharField(max_length=600, blank=False, null=False)

    def __str__(self):
        return '%s' % self.descripcion

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipo de Documentos'
