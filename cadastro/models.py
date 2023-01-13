from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cadastro1(models.Model):
    empresa = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y')
    cidade = models.CharField(max_length=30)
    salario = models.FloatField()
    localidade = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)