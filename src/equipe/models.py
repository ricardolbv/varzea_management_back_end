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
    email = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    estado = models.CharField(max_length=40)
    psw = models.CharField(max_length=40, default='123456')
    time = models.OneToOneField(
        Time, on_delete=models.CASCADE
    )  # Chave estrangeira não pode ser null


"""Representação do Objeto Capitão no Swagger"""
CapitaoAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "nome": openapi.Schema(type=openapi.TYPE_STRING),
        "email": openapi.Schema(type=openapi.TYPE_STRING,),
        "telefone": openapi.Schema(type=openapi.TYPE_STRING),
        "estado": openapi.Schema(type=openapi.TYPE_STRING),
        "psw": openapi.Schema(type=openapi.TYPE_STRING),
        "time": TimeAPIFields,
    },
)

"""Representação do Objeto Capitão no Swagger"""
LoginCapitaoAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING,),
        "psw": openapi.Schema(type=openapi.TYPE_STRING),
    },
)

class Partida(models.Model):
    times = models.ManyToManyField("Time", related_name="partidas")
    modalidade = models.CharField(max_length=25)
    dia = models.CharField(max_length=25)
    local = models.CharField(max_length=50)
    aceite = models.CharField(max_length=25, default="Aguardando")
    id_mando = models.IntegerField()

"""Representação do Objeto Partida no Swagger"""
PartidaAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "idTime1": openapi.Schema(type=openapi.TYPE_INTEGER, blank=False, default=""),
        "idTime2": openapi.Schema(type=openapi.TYPE_INTEGER, blank=False, default=""),
        "modalidade": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default=""),
        "dia": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default=""),
        "local": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default=""),
        "aceite": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default="Aguardando"),
    },
)

"""Representação do Objeto Partida no Swagger"""
UpdatePartidaAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "aceite": openapi.Schema(type=openapi.TYPE_STRING, blank=False, default="Aguardando"),
    },
)


