from django.db import models

# Create your models here.

class Formulario(models.Models):
    nome = models.CharField(max_length=100)
    email = models.TextField()
    endereco = models.TextField()
    cidade = models.TextField()
    telefone = models.TextField(null=True)
    assunto = models.TextField(max_length=100)
    mensagem = models.TextField(blank=True, null=True)