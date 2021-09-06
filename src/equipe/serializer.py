from django.db.models import fields
from rest_framework import serializers
from .models import Capitao


class CapitaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitao
        fields = '__all__'
