from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length = 30)
    rg = models.CharField(max_length = 9)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE, null = True)
    nome = models.CharField(max_length = 30)
    rg = models.CharField(max_length = 9)

    def __str__(self):
        return self.nome
