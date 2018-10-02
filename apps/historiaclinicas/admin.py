from django.contrib import admin

from .models import HistoriaClinica


class HistoriaClinicaAdmin(admin.ModelAdmin):

	list_display = [
		'fecha',
		'hora'
	]

	list_filter = [
		'fecha',
		'hora'
	]

admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)
