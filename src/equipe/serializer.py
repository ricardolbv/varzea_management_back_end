from django.db.models import fields, query
from rest_framework import serializers

from .models import Capitao, Time, Jogador, Partida


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ("id", "nome", "posicao", "jogos", "gols")


class PartidaSerializer(serializers.ModelSerializer):
    #times = Time(read_only=True, many=True)
    times = serializers.PrimaryKeyRelatedField(queryset=Time.objects.all(), many=True)

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



class TimeSerializer(serializers.ModelSerializer):
    jogadores = JogadorSerializer(source="jogador_set", many=True, read_only=True)
    partidas = PartidaSerializer(many=True, read_only=True)

    class Meta:
        model = Time
        fields = ("id", "nome", "local", "modalidade", "data", "jogadores", "partidas")


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

