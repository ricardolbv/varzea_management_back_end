from django.db.models import fields
from rest_framework import serializers

from .models import Capitao, Time, Jogador, Partida


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ("id", "nome", "posicao", "jogos", "gols")


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

class PartidaSerializer(serializers.ModelSerializer):
    #times = TimeSerializer(source='time_set', many=True)
    times = TimeSerializer(read_only=True, many=True)

    class Meta:
        model = Partida
        fields = (
            "id",
            "times",
            "modalidade",
            "mando",
            "dia",
            "local",
            "aceite",
        )

