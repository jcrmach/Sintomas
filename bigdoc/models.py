from django.db import models

# Create your models here.


class Doenca(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    ordem = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"


class Sintoma(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    ordem = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"
