from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Doencas(models.Model):
    nome = models.CharField(max_length=50)
    sintomas = models.ManyToManyField('Sintomas')


class Sintomas(models.Model):
    nome = models.CharField(max_length=50)


class Pesos(models.Model):
    doenca = models.ForeignKey(
        Doencas,
        on_delete=models.CASCADE
    )
    sintoma = models.ForeignKey(
        Sintomas,
        on_delete=models.CASCADE
    )

    class Peso(models.IntegerChoices):
        MUITO_RARO = 1
        RARO = 2
        POUCO_COMUM = 3
        COMUM = 4
        MUITO_COMUM = 5

    peso = models.PositiveSmallIntegerField(choices=Peso.choices)
