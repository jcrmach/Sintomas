### Preencher banco de dados

```python
python manage.py shell
from bigdoc.models import *

Sintoma.objects.create(nome="Febre", ordem=0)
Sintoma.objects.create(nome="Tosse", ordem=1)
Sintoma.objects.create(nome="Dor de cabeça", ordem=2)
Sintoma.objects.create(nome="Perda do paladar", ordem=3)
Sintoma.objects.create(nome="Falta de ar", ordem=4)


Doenca.objects.create(nome="Gripe", ordem=0)
Doenca.objects.create(nome="Covid-19", ordem=1)
Doenca.objects.create(nome="Resfriado", ordem=2)

```
