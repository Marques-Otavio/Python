import copy

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
    ]

def mostrar_produtos(produtos):
    for item in produtos:
        print(f"{item['nome']} - R$ {item['preco']}")
    print() 

mostrar_produtos(novos_produtos)


# # Ordene os produtos por nome decrescente (do maior para menor)
# # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos),
    key=lambda produto: produto['nome'], reverse=True) 

mostrar_produtos(produtos_ordenados_por_nome)

# # Ordene os produtos por preco crescente (do menor para maior)
# # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto ['preco']
    )

mostrar_produtos(produtos_ordenados_por_preco)















