from rest_framework import serializers
from .models import Aprendiz, Programa

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'

class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        fields = '__all__'