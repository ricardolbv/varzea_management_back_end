from django.urls import path
from . import views


urlpatterns = [
    path('capitao/', views.createCaptao),
    path('capitaes/', views.allCaptaes),
    path('capitao/<str:key>', views.getCapitaoById),
]
