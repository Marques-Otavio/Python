# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100

'''Forma abaixo faz a mesma coisa que o filter, porem com list comprehension'''
# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]

'''Agora utilizando o filter'''
novos_produtos = filter( #primeiro passa uma funcao (ex: lambda) e apos isso coloca um iteravel
    # lambda produto: produto['preco'] > 100, 
    filtrar_preco, #utilizando uma funcao nao-anonima que faz a mesma coisa que a lambda comentada acima
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)