# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



def zipper(lista1, lista2):
    intervalo_max = min(len(lista1), (len(lista2)))
    return [
        (lista1[i], lista2[i]) for i in range (intervalo_max)
    ]

from itertools import zip_longest


lista1=['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2=['BA', 'SP', 'MG', 'RJ']
print(zipper(lista1,lista2)) #utilizando a funcao criada la no inicio

print(list(zip(lista1,lista2))) #todo o codigo da funcao zipper substituido por essa funcao zip

print(list(zip_longest(lista1,lista2, fillvalue='Rio de Janeiro')))
 # zip_longest junta as listas porem pegando o valor da maior lista como base, 
 # por esse motivo foi usado esse fillvalue, pois sem ele o RJ iria ficar com valor None