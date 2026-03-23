# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

'''
combinations -> junta em grupos, mas nao repete os mesmos resultados ex: (Joao, Joana) NAO PUXARA (Joana, Joao)
permutations -> junta em grupos, no entanto, ira repetir ex: (Otavio, Augusto) PUXARA TAMBEM (Augusto, Otavio)
product -> combina todos os indices nas listas
'''

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]



print(*list(combinations(pessoas, 2)), sep='\n') #o * expande a lista para o nosso separador colocar uma quebra de linha
#no codigo acima, o combinations esta pegando todas as pessoas e combinando-as em grupos de 2, se colocasse 3 iria juntar em tres e assim por diante

def print_iter(iterator):# essa funcao serve somente para imprimir da mesma forma da linha acima, a fim de facilitar
    print(*list(iterator), sep='\n')

print_iter(combinations(pessoas, 3)) #assim so precisa chamar a funcao, nao precisara colocar em lista e separadores toda vez
print_iter(permutations(pessoas, 3))



#utilizando o product para combinar todas essas opcoes de camisetas
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]
print_iter(product(*camisetas)) #ele vai unir indice 0 com 0, com 0, 1 com 1, com 1......