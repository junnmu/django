from django.shortcuts import get_object_or_404, render

from estagio.models import Professor, Aluno

def index(request):
    return render(request, 'estagio/index.html')

def aluno_por_id(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk = aluno_id)
    return render(request, 'estagio/aluno/aluno.html', {'aluno': aluno})

def professores(request, aluno_id):
    professores = Professor.objects.order_by('nome')[:3]
    aluno = get_object_or_404(Aluno, pk = aluno_id)
    return render(request, 'estagio/aluno/professores.html', {'aluno': aluno, 'professores': professores})

def professor_por_id(request, aluno_id, professor_id):
    professor = get_object_or_404(Professor, pk = professor_id)
    aluno = get_object_or_404(Aluno, pk = aluno_id)
    return render(request, 'estagio/aluno/professor.html', {'aluno': aluno, 'professor': professor})

def solicitar_orientacao(request, aluno_id, professor_id):
    professor = get_object_or_404(Professor, pk = professor_id)
    aluno = get_object_or_404(Aluno, pk = aluno_id)
    return render(request, 'estagio/aluno/solicitar.html', {'aluno': aluno, 'professor': professor})