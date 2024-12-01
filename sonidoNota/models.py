from django.db import models

# Create your models here.
class SonidoNota(models.Model):
    nota = models.CharField(max_length=5)
    instrumento = models.CharField(max_length=100)
    sonido_url = models.URLField()