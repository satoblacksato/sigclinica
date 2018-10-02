from django.contrib import admin

from .models import Mensaje


class MensajeAdmin(admin.ModelAdmin):

	list_filter = [
		'mensaje'
	]

admin.site.register(Mensaje, MensajeAdmin)
