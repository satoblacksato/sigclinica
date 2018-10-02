from django.contrib import admin

from .models import Paciente, ObraSocial


class ObraSocialAdmin(admin.ModelAdmin):

	list_display = [
		'descripcion'
	]

	search_file = [
		'descripcion'
	]


class PacienteAdmin(admin.ModelAdmin):

	list_display = [
		'nombre',
		'apellido'
	]

	search_file = [
		'nombre',
		'apellido'
	]


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(ObraSocial, ObraSocialAdmin)
