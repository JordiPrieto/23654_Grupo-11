from django.db import models
from django.contrib.auth.models import AbstractUser


class Consulta(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return f"Consulta de {self.nombre}"

class CustomUser(AbstractUser):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username