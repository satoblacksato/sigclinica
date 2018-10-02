from django.views.generic import TemplateView

from .models import TipoDocumento


class TipoDocumentoTemplateView(TemplateView):

    template_name = 'tipo_documento_view.html'


class ObraSocialTemplateView(TemplateView):

	template_name = 'obra_social_view.html'
