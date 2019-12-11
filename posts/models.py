from django.db import models
from django.utils import timezone

class Postagem(models.Model):
    
    opcao_tema = [
        ('ROM', 'Romance'),
        ('GAM', 'Games'),
        ('PRO', 'Profissão'),
    ]

    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default = 1)
    email = models.CharField(max_length = 50)
    texto_blod = models.CharField(max_length = 150)
    tema = models.CharField(max_length = 3, choices = opcao_tema)
    ativo = models.BooleanField(default = True)
    
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    metodo_pagamento = [
        ('AV', 'Pagamento à vista'),
        ('P2', 'Parcelamento em 2x'),
        ('P3', 'Parcelamento em 3x')
    ]
    nome = models.CharField(max_length = 140)
    email = models.EmailField()
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length = 2, choices = metodo_pagamento)
    criado_em = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nome