from django.urls import path
from . import views


urlpatterns = [
    path('capitao/', views.createCaptao, name='new-capitao'),
    path('capitaes/', views.allCaptaes),
    path('capitao/<str:key>', views.getCapitaoById),
]
