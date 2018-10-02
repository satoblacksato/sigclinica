from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response

from apps.library.pagination import ChatPagination

from .serializer import MensajeSerializer, MensajeListSerializer, UsuarioSerializer
from .models import Mensaje


class MensajeViewSet(viewsets.ModelViewSet):

	queryset = Mensaje.objects.all().order_by('-id')
	serializer_class = MensajeSerializer
	pagination_class = ChatPagination

	def get_serializer_class(self):
		if self.action == 'list':
			return MensajeListSerializer
		else:
			return MensajeSerializer

	def create(self, request):
		
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			usuario = User.objects.get(pk=request.session['id_usuario'])
			mensaje_nuevo = Mensaje.objects.create(mensaje=serializer.data['mensaje'], emisor=usuario)
			mensaje = Mensaje.objects.get(pk=mensaje_nuevo.id)
			serializer = self.serializer_class(mensaje)
			return Response(serializer.data)

		return Response({
			'status': 'Bad request',
			'message': 'Account could not be created with received data.'
		}, status=status.HTTP_400_BAD_REQUEST)

	'''def list(self, request):
		
		queryset = Mensaje.objects.all()
		serializer = MensajeListSerializer(queryset, many=True)
		return Response(serializer.data)'''


class UsuarioViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all()
	serializer_class = UsuarioSerializer
