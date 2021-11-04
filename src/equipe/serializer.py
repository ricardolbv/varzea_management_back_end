from django.db.models import fields, query
from rest_framework import serializers

from .models import Capitao, Time, Jogador, Partida, Sumula, Gol, Cartao


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ("id", "nome", "posicao", "jogos", "gols")


class PartidaSerializer(serializers.ModelSerializer):
    times = serializers.PrimaryKeyRelatedField(queryset=Time.objects.all(), many=True)

    class Meta:
        model = Partida
        fields = (
            "id_mando",
            "id",
            "times",
            "modalidade",
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
            "email",
            "nome",
            "telefone",
            "estado",
            "psw",
            "time",
        )
        depth = 1


class GolSerializer(serializers.ModelSerializer):
    autor = JogadorSerializer(read_only=True, many=False)
    
    class Meta:
        model = Gol
        fields = (
            "id",
            "autor",
            "quantidade",
        )

class CartaoSerializer(serializers.ModelSerializer):
    jogador = JogadorSerializer(read_only=True, many=False)
    
    class Meta:
        model = Cartao
        fields = (
            "id",
            "tipo",
            "jogador",
        )

class SumulaSerializer(serializers.ModelSerializer):
    partida = PartidaSerializer(read_only=True, many=False)
    gols = GolSerializer(source="gol_set", many=True, read_only=True)
    cartoes = CartaoSerializer(source="cartao_set", many=True, read_only=True)

    class Meta:
        model = Sumula
        fields = (
            "id",
            "resultado",
            "aceite",
            "status",
            "partida",
            "gols",
            "cartoes",
        )
        depth = 1