# Generated by Django 3.2.6 on 2021-10-18 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0009_partida_id_mando'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='mando',
        ),
    ]
