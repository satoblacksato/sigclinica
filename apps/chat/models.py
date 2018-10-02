from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):

	emisor = models.ForeignKey(User, null=True, blank=True)
	mensaje = models.TextField(max_length=3000, null=True, blank=True)
	fecha = models.DateField(auto_now_add=True, null=True,blank=True)
	hora = models.TimeField(auto_now_add=True, null=True, blank=True)
	leido = models.BooleanField(default=False)

	def __str__(self):

		return '%s' % self.mensaje

	class Meta:
		verbose_name = 'Mensaje'
		verbose_name_plural = 'Mensajes'
