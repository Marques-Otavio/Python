# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


total = reduce( # primeiro passa uma funcao, depois o iteravel, e o valor inicial
    lambda ac, p: ac + p['preco'], #1- funcao
    produtos, #2- iterave
    0 #3- valor inicial
)

print('Total é', total)

'''Aqui faz a mesma coisa que o reduce, porem utilizando logica e for'''
# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

'''Mesma coisa que o Reduce, porem direto no print, com sum, e list comprehension'''
# print(sum([p['preco'] for p in produtos]))