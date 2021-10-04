from django.db import models
from drf_yasg import openapi


class Time(models.Model):
    nome = models.CharField(max_length=50, blank=True)
    local = models.CharField(max_length=50, blank=True)
    modalidade = models.CharField(max_length=50, blank=True)
    data = models.CharField(max_length=50, blank=True)
    vice_capitao = models.CharField(max_length=50, blank=True)


"""Representação do Objeto Equipe no Swagger"""
TimeAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "nome": openapi.Schema(type=openapi.TYPE_STRING, blank=True, default=""),
        "local": openapi.Schema(type=openapi.TYPE_STRING, blank=True, default=""),
        "modalidade": openapi.Schema(type=openapi.TYPE_STRING, blank=True, default=""),
        "data": openapi.Schema(type=openapi.TYPE_STRING, blank=True, default=""),
        "vice_capitao": openapi.Schema(
            type=openapi.TYPE_STRING, blank=True, default=""
        ),
    },
)


class Jogador(models.Model):
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING, null=True)
    nome = models.CharField(max_length=50)
    posicao = models.CharField(max_length=25)
    jogos = models.PositiveIntegerField(default=0)
    gols = models.PositiveIntegerField(default=0)


"""Representação do Objeto Jogador no Swagger"""
JogadorAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "nome": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default=""),
        "posicao": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default=""),
    },
)


class Capitao(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=25)
    telefone = models.CharField(max_length=25)
    endereco = models.CharField(max_length=35)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=35, blank=True)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=40)
    cep = models.CharField(max_length=40)
    time = models.OneToOneField(
        Time, on_delete=models.CASCADE
    )  # Chave estrangeira não pode ser null


"""Representação do Objeto Capitão no Swagger"""
CapitaoAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "nome": openapi.Schema(type=openapi.TYPE_STRING),
        "cpf": openapi.Schema(type=openapi.TYPE_STRING),
        "telefone": openapi.Schema(type=openapi.TYPE_STRING),
        "endereco": openapi.Schema(type=openapi.TYPE_STRING),
        "numero": openapi.Schema(type=openapi.TYPE_INTEGER),
        "complemento": openapi.Schema(type=openapi.TYPE_STRING),
        "cidade": openapi.Schema(type=openapi.TYPE_STRING),
        "estado": openapi.Schema(type=openapi.TYPE_STRING),
        "cep": openapi.Schema(type=openapi.TYPE_STRING),
        "time": TimeAPIFields,
    },
)
