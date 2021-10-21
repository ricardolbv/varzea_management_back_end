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
    Partida,
    CapitaoAPIFields,
    LoginCapitaoAPIFields,
    TimeAPIFields,
    JogadorAPIFields,
    PartidaAPIFields,
    UpdatePartidaAPIFields,
)
from .serializer import CapitaoSerializer, TimeSerializer, JogadorSerializer, PartidaSerializer


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
            telefone=request.data["telefone"],
            estado=request.data["estado"],
            psw=request.data["psw"],
            email=request.data["email"],
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


@swagger_auto_schema(
    methods=["put"],
    responses={
        200: "Jogador atualizado com sucesso",
        404: "Jogador não encontrado",
        400: "Erro ao atualizar Jogador",
    },
    request_body=JogadorAPIFields,
)
@api_view(["PUT"])
def updateJogadorById(request, key):
    """Atualiza o jogador com base no ID passado por parâmetro"""
    try:
        jogador = Jogador.objects.get(id=key)
    except:
        return Response(data="Jogador inexistente", status="404")

    serializer = JogadorSerializer(jogador, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status="200")

    return Response(data=serializer.errors, status="400")


@swagger_auto_schema(
    methods=["delete"],
    responses={
        200: "Jogador excluido com sucesso",
        404: "Jogador não encontrado",
        400: "Erro ao atualizar Jogador",
    },
)
@api_view(["DELETE"])
def deleteJogadorById(request, key):
    """Exclui o jogador com base no ID passado por parâmetro"""
    try:
        Jogador.objects.get(id=key).delete()
    except:
        return Response(data="Jogador inexistente", status="404")

    return Response(data="Jogador deletado", status="200")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Times retornados com sucesso",
        404: "Erro ao retornar os times",
        400: "Time inexistente",
    },
)
@api_view(["GET"])
def getTimesParaJogar(request, key):
    """Retorna times disponiveis para jogo com base no ID de um time"""
    try:
        Time.objects.get(id=key)

    except:
        return Response(data="Time inexistente", status="400")

    try:
        times = Time.objects.all()

        times_dispo = (
            [  # Regra de nócio: Retorno times que possuem nome diferente de ""
                time for time in times if int(time.id) != int(key) and time.nome != ""
            ]
        )
        serializer = TimeSerializer(times_dispo, many=True)

        return Response(data=serializer.data, status="200")

    except:
        return Response(data="Erro ao retornar os times", status="404")


@swagger_auto_schema(
    methods=["post"],
    responses={
        200: "Partida criada com sucesso",
        404: "Time não encontrado",
        400: "Erro ao criar jogo",
    },
    request_body=PartidaAPIFields,
)
@api_view(["POST"])
def createPartida(request):
    """Cria uma partida com base no id de dois times passados por pârametro"""
    try:
        time1 = Time.objects.get(id=request.data["idTime1"])
        time2 = Time.objects.get(id=request.data["idTime2"])
        
    except:
        return Response(data="Time inexistente", status="404")

    partida = Partida.objects.create(
        id_mando=request.data["idTime1"],
        modalidade=request.data["modalidade"],
        dia=request.data["dia"], local=request.data["local"], aceite=request.data["aceite"]
    )

    #Adicionando equipes ao objeto
    try:
        partida.times.add(time1, time2)
        serializer = PartidaSerializer(data=model_to_dict(partida))

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status="200")

        resp = Partida.objects.get(id=partida.id)
        resp = PartidaSerializer(instance=resp)

        return Response(data=resp.data, status="200")

    except Exception as err:
        return Response(data=err, status="400")


@swagger_auto_schema(
    methods=["get"],
    responses={
        200: "Retorna partida com sucesso",
        404: "Erro ao retornar partida",
        400: "Partida inexistente",
    },
)
@api_view(["GET"])
def getParidaByID(request, key):
    """Retorna Partida por id"""
    try:
        resp = Partida.objects.get(id=key)

    except:
        return Response(data="Partida inexistente", status="400")

    try:
        serializer = PartidaSerializer(instance=resp)
        print(serializer.data['times'])

        return Response(data=serializer.data, status="200")

    except:
        return Response(data="Erro ao retornar partida", status="404")


@swagger_auto_schema(
    methods=["put"],
    responses={
        200: "Partida atualizada com sucesso",
        404: "Partida não encontrada",
        400: "Erro ao atualizar Partida",
    },
    request_body=UpdatePartidaAPIFields,
)
@api_view(["PUT"])
def updatePartidaById(request, key):
    """Atualiza a partida com base no id"""
    try:
        partida = Partida.objects.get(id=key)
    except:
        return Response(data="Partida inexistente", status="404")

    serializer = PartidaSerializer(partida, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(data=serializer.data, status="200")

    return Response(data=serializer.errors, status="400")


@swagger_auto_schema(
    methods=["post"],
    responses={
        200: "Capitaes deletados",
        400: "Erro ao excluir Capitães",
    },
)
@api_view(["POST"])
def deleteAllCaptains(request):
    """Exclui todos os capitães do sistema"""
    try:
        Capitao.objects.all().delete()

        return Response(data={'Sucesso. Todos os capitães foram deletados'}, status="200")

    except:
        return Response(data="Erro ao deletar", status="404")


@swagger_auto_schema(
    methods=["post"],
    responses={
        200: "Capitão logado",
        404: "Erro de credencial",
        400: "Capitão inexistente",
    },
    request_body=LoginCapitaoAPIFields
)
@api_view(["POST"])
def login(request):
    """Loga no sistema com base no email e senha"""
    try:
        resp = Capitao.objects.get(email=request.data['email'])
        serializer = CapitaoSerializer(resp, many=False)

        if not serializer.data.__len__:
            return Response(data="Capitão inexistente", status="400")

        cpt = model_to_dict(resp)
        if(cpt['psw'] == request.data['psw']):
            return Response(data=serializer.data, status="200")

        return Response(data="Erro de credencial", status="404")

    except:
        return Response(data="Erro", status="500")

