from rest_framework import serializers

from .models import HistoriaClinica


class HistoriaClinicaCreateSerializer(serializers.ModelSerializer):


	class Meta:
		model = HistoriaClinica
		fields = '__all__'
