from django import forms

from .models import Turno

class TurnoForm(forms.ModelForm):

	class Meta:
		fields = ['paciente', 'title', 'backgroundColor', 'start', 'empleado', 'estado']
