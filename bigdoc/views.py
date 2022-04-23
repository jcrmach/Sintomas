from django.shortcuts import render

from .models import Sintoma
from .util import diagnosticar

# Create your views here.


def index(request):
    if request.method == 'POST':
        sintomas = request.POST.getlist("sintomas")
        diagnostico = diagnosticar(sintomas)

        return render(request, 'bigdoc/diagnostico.html', {
            'sintomas_list': sintomas,
            'diagnostico': diagnostico
        })

    return render(request, 'bigdoc/index.html', {
        'sintomas': Sintoma.objects.all(),
    })
