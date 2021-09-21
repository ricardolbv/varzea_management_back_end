from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict

from datetime import datetime

from .models import (
    Capitao,
    Time,
    Jogador,
    CapitaoAPIFields,
    TimeAPIFields,
    JogadorAPIFields,
)
from .serializer import CapitaoSerializer, TimeSerializer, JogadorSerializer


@swagger_auto_schema(
    methods=["post"],
    responses={
        201: "Capitão criado com sucesso",
        400: "Erro ao criar capitão",
        404: "Conteudo de criação incorreta para recurso",
    },
    request_body=CapitaoAPIFields,
)
@api_view(["POST"])
def createCaptao(request):
    """Cria capitão"""
    try:
        if request.data["time"]["data"] is "":
            request.data["time"]["data"] = datetime.today().strftime("%Y-%m-%d")

        new_time = Time.objects.create(
            nome=request.data["time"]["nome"],
            local=request.data["time"]["local"],
            modalidade=request.data["time"]["modalidade"],
            data=request.data["time"]["data"],
        )
        new_time.save()

        new_capitao = Capitao.objects.create(
            nome=request.data["nome"],
            cpf=request.data["cpf"],
            telefone=request.data["telefone"],
            endereco=request.data["endereco"],
            numero=request.data["numero"],
            complemento=request.data["complemento"],
            cidade=request.data["cidade"],
            estado=request.data["estado"],
            cep=request.data["cep"],
            time=new_time,
        )

        serializer = CapitaoSerializer(data=model_to_dict(new_capitao))

    except Exception as err:
        return Response(data=err, status="400")

    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status="201")
        except:
            response = Capitao.objects.get(id=model_to_dict(new_capitao)["id"])
            _serializer = CapitaoSerializer(response, many=False)

            return Response(
                _serializer.data, status="201"
            )  # Bypass: erro de integridade do msql

    return Response(serializer.errors, status="404")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Retorna todos os capitães",
        400: "Erro ao retornar todos os capitães",
    },
)
@api_view(["GET"])
def allCaptaes(request):
    """Retorna todos os capitães criados"""
    try:
        allCpts = Capitao.objects.all()
        serializer = CapitaoSerializer(allCpts, many=True)
        return Response(data=serializer.data, status="200")
    except:
        return Response(data="Erro ao retornar todos os capitães", status="400")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Retorna o capitão com base no ID",
        404: "Capitão não encontrado",
        400: "Erro ao retornar capitão",
    },
)
@api_view(["GET"])
def getCapitaoById(request, key):
    """Retorna o capitão com base no ID"""
    try:
        cpt = Capitao.objects.get(id=key)
        serializer = CapitaoSerializer(cpt, many=False)
        if serializer.data.__len__:
            return Response(data=serializer.data, status="200")
    except:
        return Response(data="Nenhum capitão com esse ID", status="404")


@swagger_auto_schema(
    methods=["put"],
    responses={
        202: "Time atualizado com sucesso",
        404: "Time não encontrado",
        400: "Erro ao atualizar time",
    },
    request_body=TimeAPIFields,
)
@api_view(["PUT"])
def updateTimeById(request, key):
    """Atualiza o time com base no ID passado por parâmetro"""
    try:
        time = Time.objects.get(id=key)
    except:
        return Response(data="Time inexistente", status="404")

    serializer = TimeSerializer(time, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status="200")

    return Response(data=serializer.errors, status="400")


@swagger_auto_schema(
    methods=["post"],
    responses={
        200: "Jogador criado com",
        404: "Time não encontrado",
        400: "Erro ao atualizar time",
    },
    request_body=JogadorAPIFields,
)
@api_view(["POST"])
def createPlayerOnIDTeam(request, key):
    """Cria um jogador com base no ID do time passado"""
    try:
        time = Time.objects.get(id=key)
    except:
        return Response(data="Time inexistente", status="404")

    jogador = Jogador.objects.create(
        nome=request.data["nome"], posicao=request.data["posicao"], time=time
    )

    serializer = JogadorSerializer(data=model_to_dict(jogador))

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status="200")

    return Response(data=serializer.errors, status="400")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Retorna o time com base no ID",
        404: "Time não encontrado",
        400: "Erro ao retornar time",
    },
)
@api_view(["GET"])
def getTimeById(request, key):
    """Retorna o time com base no ID"""
    try:
        time = Time.objects.get(id=key)
    except:
        return Response(data="Time inexistente", status="404")

    serializer = TimeSerializer(instance=time)
    return Response(data=serializer.data, status="200")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Retorna o jogador com base no ID",
        404: "Jogador não encontrado",
        400: "Erro ao retornar jogador",
    },
)
@api_view(["GET"])
def getJogadorById(request, key):
    """Retorna o jogador com base no ID"""
    try:
        jogador = Jogador.objects.get(id=key)
    except:
        return Response(data="Jogador inexistente", status="404")

    serializer = JogadorSerializer(instance=jogador)
    return Response(data=serializer.data, status="200")
