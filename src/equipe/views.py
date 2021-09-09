from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Capitao, CapitaoAPIFields
from .serializer import CapitaoSerializer


@swagger_auto_schema(methods=['post'], responses={201: 'Capitão criado com sucesso', 400: 'Erro ao criar capitão', 404: 'Conteudo de criação incorreta para recurso'},
                     request_body=CapitaoAPIFields)
@api_view(['POST'])
def createCaptao(request):
    """Cria capitão"""
    try:
        serializer = CapitaoSerializer(data=request.data)
    except:
        return Response(data='Erro ao criar novo capitão', status='400')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status='201')
    return Response("Conteudo de criação incorreta para recurso", status='404')


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
