import json
from django.http import response

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from equipe.models import Capitao
from equipe.serializer import CapitaoSerializer


class PositiveCaptainTestCases(APITestCase):
    """ Test module for retrieve responses different than 200 HTTP responses """

    URL = reverse('new-capitao')

    def test_captain_creation_with_out_complemento(self):
        data = {'nome': 'capitao_teste', 'cpf': '476.441.228-42', 'telefone': '19998976687', 'endereco': 'testAddress', 'numero': '526',
                'complemento': '',  'cidade': 'campinas', 'estado': 'SP', 'cep': '13052-577'}
        response = self.client.post(self.URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(response.data))

    def test_captain_creation_with_complemento(self):
        data = {'nome': 'capitao_teste', 'cpf': '476.441.228-42', 'telefone': '19998976687', 'endereco': 'testAddress', 'numero': '526',
                'complemento': 'Test',  'cidade': 'campinas', 'estado': 'SP', 'cep': '13052-577'}
        response = self.client.post(self.URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(response.data))


class NegativeCapatainTestCases(APITestCase):
    """ Test module for retrieve responses different than 200 HTTP responses """

    URL = reverse('new-capitao')

    def test_captain_miss_field(self):
        data = {'cpf': '476.441.228-42', 'telefone': '19998976687', 'endereco': 'testAddress', 'numero': '526',
                'complemento': '',  'cidade': 'campinas', 'estado': 'SP', 'cep': '13052-577'}
        response = self.client.post(self.URL, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(
            response.data, "Conteudo de criação incorreta para recurso")


class RetrieveCaptainsTestCases(APITestCase):
    """ Test module for retrieve Capatains/Captain endpoint """

    URL_CREATE = reverse('new-capitao')
    URL_ALL = reverse('all-capitaes')

    def setUp(self):
        self.valid_payload = {
            'nome': 'capitao_teste',
            'cpf': '476.441.228-42',
            'telefone': '19998976687',
            'endereco': 'testAddress',
            'numero': '526',
            'complemento': 'Test',
            'cidade': 'campinas',
            'estado': 'SP',
            'cep': '13052-577'
        }
        self.client.post(self.URL_CREATE, self.valid_payload)

    def test_retrive_all_captains(self):
        response = self.client.get(self.URL_ALL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
