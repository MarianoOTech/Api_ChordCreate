from django.db import models
import json

class Escala(models.Model):
    tonalidad = models.CharField(max_length=5)
    tipo = models.CharField(max_length=10)
    notas = models.TextField()  # Cambiado de JSONField a TextField

    def __str__(self):
        return f"{self.tonalidad} {self.tipo}"

    # Método para obtener las notas como diccionario
    def get_notas_as_dict(self):
        try:
            return json.loads(self.notas)
        except json.JSONDecodeError:
            return {}

    # Método para establecer las notas desde un diccionario
    def set_notas_from_dict(self, notas_dict):
        self.notas = json.dumps(notas_dict)
