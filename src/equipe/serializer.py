from django.db.models import fields
from rest_framework import serializers

from .models import Capitao, Time, Jogador


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ("id", "nome", "posicao")


class TimeSerializer(serializers.ModelSerializer):
    jogadores = JogadorSerializer(source="jogador_set", many=True, read_only=True)

    class Meta:
        model = Time
        fields = ("id", "nome", "local", "modalidade", "data", "jogadores")


class CapitaoSerializer(serializers.ModelSerializer):
    time = TimeSerializer(read_only=True, many=False)

    class Meta:
        model = Capitao
        fields = (
            "id",
            "nome",
            "cpf",
            "telefone",
            "endereco",
            "numero",
            "complemento",
            "cidade",
            "estado",
            "cep",
            "time",
        )
        depth = 1
