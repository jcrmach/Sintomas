from django.db import models

# Create your models here.


class Diagnostico(models.Model):
    doenca = models.ForeignKey(
        'Doenca',
        on_delete=models.CASCADE,
        related_name="diagnostico"
    )
    sintoma = models.ForeignKey(
        'Sintoma',
        on_delete=models.CASCADE,
        related_name="diagnostico"
    )

    class Peso(models.IntegerChoices):
        MUITO_RARO = 1
        RARO = 2
        POUCO_COMUM = 3
        COMUM = 4
        MUITO_COMUM = 5

    peso = models.PositiveSmallIntegerField(choices=Peso.choices)

    def __str__(self):
        return f"{self.doenca} e {self.sintoma} - {self.peso}"


class Doenca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome}"


class Sintoma(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome}"
