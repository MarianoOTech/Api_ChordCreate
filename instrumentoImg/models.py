from django.db import models

# Create your models here.
class InstrumentoImagen(models.Model):
    nota = models.CharField(max_length=5)
    instrumento = models.CharField(max_length=100)
    imagen_url = models.URLField()