import importlib

import Aula98_Auxiliar

print(Aula98_Auxiliar.variavel)

for i in range(10):
    importlib.reload(Aula98_Auxiliar)
    print(i)

print('Fim')