from django.views.generic import TemplateView

from .models import Paciente


class PacienteTemplateView(TemplateView):

    template_name = 'paciente_view.html'
