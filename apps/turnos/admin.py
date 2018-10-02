from django.contrib import admin

from .models import Turno


class TurnoAdmin(admin.ModelAdmin):

	list_display = [
		'title',
		'start',
		'end',
		'allDay'
	]

	list_filter = [
		'title',
		'start',
		'end',
		'allDay'
	]


admin.site.register(Turno, TurnoAdmin)
