import uuid
from django.db import models
from django.utils import timezone

class Piada(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    titulo = models.CharField(max_length=200)

    conteudo = models.CharField(max_length=200)

    categoria = models.CharField(max_length=20)

    createdAt = models.DateTimeField(auto_now_add=True)

# class Usuario(models.Model):
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     titulo = models.CharField(max_length=200)
#
#     data = start = models.DateTimeField( verbose_name='Data de Nascimento' )
