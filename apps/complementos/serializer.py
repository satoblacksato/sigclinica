
from rest_framework import serializers

from .models import TipoDocumento

from apps.pacientes.models import ObraSocial


class TipoDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDocumento
        fields = '__all__'


class ObraSocialSerializer(serializers.ModelSerializer):

	class Meta:
		model = ObraSocial
		fields = '__all__'