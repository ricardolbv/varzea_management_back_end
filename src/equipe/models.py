from django.db import models
from drf_yasg import openapi


class Capitao(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=25)
    telefone = models.CharField(max_length=25)
    endereco = models.CharField(max_length=35)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=35, blank = True)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    cep = models.CharField(max_length=40)


"""Representação do Objeto no Swagger"""
CapitaoAPIFields = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'nome': openapi.Schema(type=openapi.TYPE_STRING),
        'cpf': openapi.Schema(type=openapi.TYPE_STRING),
        'telefone': openapi.Schema(type=openapi.TYPE_STRING),
        'endereco': openapi.Schema(type=openapi.TYPE_STRING),
        'numero': openapi.Schema(type=openapi.TYPE_INTEGER),
        'complemento': openapi.Schema(type=openapi.TYPE_STRING),
        'cidade': openapi.Schema(type=openapi.TYPE_STRING),
        'estado': openapi.Schema(type=openapi.TYPE_STRING),
        'cep': openapi.Schema(type=openapi.TYPE_STRING),
    })
