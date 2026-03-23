
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
'''
#primeira resolucao, criando uma funcao.
def soma_listas(lista_a, lista_b):
    intervalo = min(len(lista_a), len(lista_b))
    return [ 
        (lista_a[i] + lista_b[i]) for i in range(intervalo)
    ]

print('=============== resultado')
print(soma_listas(lista_a, lista_b))
'''

#segunda resolucao, com enumerate.
'''
lista_soma  = [2, 4, 6, 8]

for i, _ in enumerate(lista_b): #o enumerate retorna uma tupla com indice e valor, por isso coloquei um '_', ele significa que quero so o indice e o valor fica de lado
    lista_soma.append(lista_a[i] + lista_b[i])

print('=============== resultado')
print(lista_soma)
'''

# MELHOR RESOLUCAO COM PYTHON
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

# utiliza uma list comprehension, essa linha faz basicamente tudo o que aquela primeira resolucao faz,
# explicando: o zip une as duas listas, deixando assim '(1, 1), (2, 2), (3, 3), (4, 4)', ou seja com o indice 0 da lista_a ao lado do indice 0 da lista_b, e assim por diante
# x, y representa os indices e soma eles para cada um que estiver em dupla, por isso nao dara os resultados dos incides que sobraram em lista_a
# somente para fins de conferencia da explicacao da linha 43:
print(list(zip(lista_a, lista_b)))