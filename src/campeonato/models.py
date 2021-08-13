from django.db import models


class Campeonato(models.Model):
    nome = models.CharField(max_length=90)
    desc = models.TextField()
