from rest_framework import viewsets

from .serializer import NotaSerializer
from .models import Nota


class NotaViewSet(viewsets.ModelViewSet):

	queryset = Nota.objects.all()
	serializer_class = NotaSerializer
