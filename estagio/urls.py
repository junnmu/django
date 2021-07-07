from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('alunos/<int:aluno_id>/', views.aluno_por_id, name = 'aluno_por_id'),
    path('alunos/<int:aluno_id>/professores/', views.professores, name = 'professores'),
    path('alunos/<int:aluno_id>/professores/<int:professor_id>/', views.professor_por_id, name = 'professor_por_id'),
    path('alunos/<int:aluno_id>/professores/<int:professor_id>/aplicar', views.solicitar_orientacao, name = 'solicitar_orientacao')
]