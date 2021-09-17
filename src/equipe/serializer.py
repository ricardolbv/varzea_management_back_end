from django.db.models import fields
from rest_framework import serializers

from .models import Capitao
from .models import Time


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = fields = ('id', 'nome', 'local', 'modalidade', 'data')



class CapitaoSerializer(serializers.ModelSerializer):
    time = TimeSerializer(read_only=True, many=False)
    
    class Meta:
        model = Capitao
        fields = ('id', 'nome', 'cpf', 'telefone', 'endereco', 'numero', 'complemento', 'cidade', 'estado', 'cep', 'time')
        depth = 1