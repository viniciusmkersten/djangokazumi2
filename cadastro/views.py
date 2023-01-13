from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadastro1


def primeira_pagina(request):
    cadastros = Cadastro1.objects.all()

    return render(request, 'cadastro/home.html', {
        'cadastros': cadastros
    })


def pagina2(request, id_cadastro):
    ver_descricao = Cadastro1.objects.get(id=id_cadastro)

    return render(request, 'cadastro/visualizar.html', {
        'ver_descricao': ver_descricao
    })


def pesquisar(request):
    lista = Cadastro1.objects.all()
    pesq = request.GET.get('pesquisa')
    if pesq:
        lista = Cadastro1.objects.filter(empresa__icontains=pesq)

    return render(request, 'cadastro/busca.html', {})


def cadastrar_usuario(request):
    return render(request, 'cadastro/cadastrar.html')


def entrar_site(request):
    return render(request, 'cadastro/login.html', )
