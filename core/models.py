from django.db import models


# Create your models here.

class Usuarios(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, unique=True, blank=False)
    senha = models.CharField(max_length=12, null=False, blank=False)

    def __str__(self):
        return self.nome
