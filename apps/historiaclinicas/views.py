
from django.views.generic import TemplateView

from apps.empleados.models import Empleado
from apps.pacientes.models import Paciente
from .models import HistoriaClinica



class HistoriaClinicaView(TemplateView):

	template_name = 'historiaclinica.html'