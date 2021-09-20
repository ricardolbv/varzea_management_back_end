from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('capitao/', views.createCaptao, name='new-capitao'),
    path('capitaes/', views.allCaptaes, name='all-capitaes'),
    path('capitao/<str:key>', views.getCapitaoById, name='one-capitao'),
    path('capitao/<str:key>/time', views.updateTimeById, name='update-time'),
]
