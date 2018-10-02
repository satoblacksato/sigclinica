
from django.views.generic import TemplateView


class TurnoView(TemplateView):

	template_name = 'turno_view.html'


class TurnoList(TemplateView):

	template_name = 'turno_list.html'


class TurnoEspontaneo(TemplateView):

	template_name = 'turno_espontaneo.html'
