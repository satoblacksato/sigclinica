from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Nota


class NotaTemplateView(TemplateView):

	template_name = 'notas.html'
