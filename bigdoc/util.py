from .models import Sintoma

from collections import Counter


def diagnosticar(sintomas):
    diag_as_peso = Counter()
    for sintoma in sintomas:
        diag_as_peso.update(diag_sintoma_as_dict(sintoma))

    return diag_to_percent(diag_as_peso).most_common()


def diag_sintoma_as_dict(sintoma):
    diagnosticos = Sintoma.objects.get(nome=sintoma).diagnostico.all()
    diag_dict = {}
    if diagnosticos is not None:
        for diagnostico in diagnosticos:
            diag_dict[diagnostico.doenca] = diagnostico.peso
        return diag_dict
    else:
        return None


def diag_to_percent(diagnostico):
    diag = diagnostico.copy()
    for key in diag:
        diag[key] = round((diagnostico[key] / sum(diagnostico.values())) * 100)
    return diag
