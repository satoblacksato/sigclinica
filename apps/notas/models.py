from django.db import models


class Nota(models.Model):

	fecha = models.DateTimeField(auto_now=True)
	nota = models.TextField(max_length=1900, null=True, blank=True)

	def __str__(self):
		return '%s - %s' % (self.fecha, self.nota)

	class Meta:
		verbose_name = 'Nota'
		verbose_name_plural = 'Notas'
