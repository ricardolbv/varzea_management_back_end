from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import Capitao, Time, CapitaoAPIFields
from .serializer import CapitaoSerializer


@swagger_auto_schema(methods=['post'], responses={201: 'Capitão criado com sucesso', 400: 'Erro ao criar capitão', 404: 'Conteudo de criação incorreta para recurso'},
                     request_body=CapitaoAPIFields)
@api_view(['POST'])
def createCaptao(request):
    """Cria capitão"""
    try:
        new_time = Time.objects.create(
            nome=request.data['time']['nome'],
            local=request.data['time']['local'],
            modalidade=request.data['time']['modalidade'],
            data=request.data['time']['data']
        )
        new_time.save()

        new_capitao = Capitao.objects.create(
            nome = request.data['nome'],
            cpf = request.data['cpf'],
            telefone = request.data['telefone'],
            endereco = request.data['endereco'],
            numero = request.data['numero'],
            complemento = request.data['complemento'],
            cidade = request.data['cidade'],
            estado = request.data['estado'],
            cep = request.data['cep'],
            time = new_time,
        )

        print(new_capitao)
        serializer = CapitaoSerializer(data = model_to_dict(new_capitao))


    except Exception as err:
        return Response(data=err, status='400')

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status='201')

    return Response(serializer.errors, status='404')


@swagger_auto_schema(methods=['get'], responses={200: 'Retorna todos os capitães', 400: 'Erro ao retornar todos os capitães'})
@api_view(['GET'])
def allCaptaes(request):
    """Retorna todos os capitães criados"""
    try:
        allCpts = Capitao.objects.all()
        serializer = CapitaoSerializer(allCpts, many=True)
        return Response(data=serializer.data, status='200')
    except:
        return Response(data='Erro ao retornar todos os capitães', status='400')


@swagger_auto_schema(methods=['get'], responses={200: 'Retorna o capitão com base no ID', 404: 'Capitão não encontrado', 400: 'Erro ao retornar capitão'})
@api_view(['GET'])
def getCapitaoById(request, key):
    """Retorna o capitão com base no ID"""
    try:
        cpt = Capitao.objects.get(id=key)
        serializer = CapitaoSerializer(cpt, many=False)
        if serializer.data.__len__:
            return Response(data=serializer.data, status='200')
    except:
        return Response(data='Nenhum capitão com esse ID', status='404')
