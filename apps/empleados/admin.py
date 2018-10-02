from django.contrib import admin

from .models import Empleado


class EmpleadoAdmin(admin.ModelAdmin):

	list_display = [
		'nombre',
		'apellido'
	]

	search_fields = [
		'nombre',
		'apellido'
	]

admin.site.register(Empleado, EmpleadoAdmin)
