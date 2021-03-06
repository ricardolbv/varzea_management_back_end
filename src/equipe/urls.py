from os import name
from django.urls import path
from . import views


urlpatterns = [
    path("capitao/", views.createCaptao, name="new-capitao"),
    path("capitaes/", views.allCaptaes, name="all-capitaes"),
    path("capitao/<str:key>/", views.getCapitaoById, name="one-capitao"),
    path("capitao/<str:key>/time", views.updateTimeById, name="update-time"),
    path(
        "capitao/<str:key>/time/jogador",
        views.createPlayerOnIDTeam,
        name="create-jogador",
    ),
    path("time/<str:key>", views.getTimeById, name="one-time"),
    path("jogador/<str:key>", views.getJogadorById, name="one-jogador"),
    path("jogador/update/<str:key>", views.updateJogadorById, name="update-jogador"),
    path("jogador/delete/<str:key>", views.deleteJogadorById, name="delete-jogador"),
    path("time/times-dispo/<str:key>", views.getTimesParaJogar, name="get-times-dispo"),
    path("partida", views.createPartida, name="create-partida"),
    path("partida/<str:key>", views.getParidaByID, name="get-partida-id"),
    path("partida/update/<str:key>", views.updatePartidaById, name="update-partida-id"),
    path("capitaes/delete", views.deleteAllCaptains, name="delete-captains"),
    path("auth", views.login, name="login"),
    path("sumulas/", views.allSumulas, name="all-sumulas"),
    path("sumula/<str:key>/partida", views.getSumulaByIDPartida, name="one-sumula"),
    path("sumula/update/<str:key>", views.updateSumulaById, name="update-sumula"),
    path("gol/create/sumula/<str:key>", views.createGoalOnIDSumula, name="goal-create"),
    path("gol/", views.allGoals, name="goal-all"),
    path("gol/partida/<str:key>", views.getGolsByIDPartida, name="goals-by-partida"),
    path("cartao/create/sumula/<str:key>", views.createCardOnIDSumula, name="card-create"),
]
