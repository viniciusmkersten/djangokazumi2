from django.urls import path
from . import views

urlpatterns = [
    path('', views.primeira_pagina, name='pagina1'),
    path('<int:id_cadastro>', views.pagina2, name='pagina2'),
    path('busca/', views.pesquisar, name='busca'),
    path('login/', views.entrar_site, name='entrar'),
    path('registro/', views.cadastrar_usuario, name='cadastrar'),
]