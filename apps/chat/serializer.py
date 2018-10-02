from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Mensaje

class UsuarioSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = '__all__'


class MensajeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Mensaje
		fields = '__all__'


class MensajeListSerializer(serializers.ModelSerializer):

	emisor = UsuarioSerializer()

	class Meta:
		model = Mensaje
		fields = '__all__'
