from .models import Sintoma, Doenca

import numpy as np
from joblib import load

from django.conf import settings


def diagnosticar(sintomas):
    knn = load(settings.BASE_DIR /
               'bigdoc/static/bigdoc/models/diagnostico.joblib')
    dados_entrada = extrair_dados(sintomas)

    prediction = knn.predict_proba(dados_entrada)

    diagnostico = {}
    for doenca in Doenca.objects.all():
        diagnostico[doenca.nome] = round(prediction[0][doenca.ordem] * 100)
    return diagnostico


def extrair_dados(sintomas):
    entrada = np.zeros(Sintoma.objects.all().count(), int)
    for sintoma in sintomas:
        sint = Sintoma.objects.get(nome=sintoma)
        entrada[sint.ordem] = 1
    return entrada.reshape(1, -1)
