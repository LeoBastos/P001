from django.db import models
from django.utils import timezone

from cliente.models import Cliente


class Servico(models.Model):
    pintura = (
        ('Azul', 'Azul'),
        ('Amarelo', 'Amarelo'),
        ('Branco', 'Branco'),
        ('Cinza', 'Cinza'),
        ('Prata', 'Prata'),
        ('Preto', 'Preto'),
        ('Dourado', 'Dourado'),
        ('Vermelho', 'Vermelho'),

    )
    fabricante = (
        ('Volkswagen', 'volkswagen'),
        ('FIAT', 'FIAT'),
        ('Chevrolet', 'Chevrolet'),
        ('General Motors', 'General Motors'),
        ('Hyundai-Kia', 'Hyundai-Kia'),
        ('Ford Motor', 'Ford Motor'),
        ('Renault', 'Renault'),
        ('Honda Motor', 'Honda Motor'),
        ('Mercedes', 'Mercedes'),
        ('Pegout', 'Pegeut'),

    )

    modelo = (
        ("Hatch", "Hatch"),
        ("Sedã", "Sedã"),
        ("SUV", "SUV"),
        ("Van", "Van"),
        ("Picape", "Picape"),
    )
    motor = (
        ("1.0", "1.0"),
        ("1.4", "1.4"),
        ("1.6", "1.6"),
        ("1.8", "1.8"),
        ("2.0", "2.0"),

    )
    combustivel = (
        ("Alcool", "Alcool"),
        ("Gasolina", "Gasolina"),
        ("Diesel", "Diesel"),
        ("Flex", "Flex"),
    )
    tipo = (
        ('Pintura', 'Pintura'),
        ('Lanternagem', 'Lanternagem'),
        ('Mecanica', 'Mecanica'),
        ('Pintura/Lanternagem', 'Pintura/Lanternagem'),
        ('Pintura/Mecaninca', 'Pintura/Mecaninca'),
        ('Lanternagem/Mecanica', 'Lanternagem/Mecanica'),
        ('Pintura/Lanternagem/Mecanica', 'Pintura/Lanternagem/Mecanica'),
    )
    nome = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='nomes')
    fabricante = models.CharField(max_length=30, choices=fabricante, blank=False)
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    ano = models.CharField(max_length=10)
    modelo = models.CharField(max_length=30, choices=modelo, blank=False)
    pintura = models.CharField(max_length=30, choices=pintura, blank=False)
    motor = models.CharField(max_length=30, choices=motor, blank=False)
    combustivel = models.CharField(max_length=30, choices=combustivel, blank=False)
    tipo = models.CharField(max_length=30, choices=tipo)
    descricao = models.TextField(max_length=300)
    solucao = models.TextField(max_length=300, blank=True)
    status = models.BooleanField(default=False)
    pecas = models.CharField(max_length=80, blank=True)
    preco = models.IntegerField(default=0)
    data_serv = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.carro
