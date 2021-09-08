import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from equipe.models import Capitao
from equipe.serializer import CapitaoSerializer


class PositiveCaptainTestCases(APITestCase):
    def test_captain_creation_right_status(self):
        URL = reverse('new-capitao')
        data = {'nome': 'capitao_teste', 'cpf': '476.441.228-42', 'telefone': '19998976687', 'endereco': 'testAddress', 'numero': '526',
                'complemento': '',  'cidade': 'campinas', 'estado': 'SP', 'cep': '13052-577'}
        response = self.client.post(URL, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
