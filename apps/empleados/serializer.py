
from rest_framework import serializers

from .models import Empleado


class EmpleadoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'
