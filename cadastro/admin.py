from django.contrib import admin
from . models import Categoria, Cadastro1

class Cadastro1Admin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'titulo', 'cidade', 'salario', 'localidade')

admin.site.register(Categoria)
admin.site.register(Cadastro1, Cadastro1Admin)
