from django.contrib import admin
from estagio.models import Aluno, Professor

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'professor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Aluno, Alunos)
admin.site.register(Professor, Professores)
