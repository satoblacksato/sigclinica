
from rest_framework import serializers

from .models import Paciente, Foto
from apps.complementos.serializer import ObraSocialSerializer


class PacienteCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Paciente
		fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Foto
		fields = '__all__'


class PacienteListSerializer(serializers.ModelSerializer):

	obra_social = ObraSocialSerializer()

	class Meta:
		model = Paciente
		fields = '__all__'
