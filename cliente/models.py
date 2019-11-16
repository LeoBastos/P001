from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    cpf = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=25, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


