import random
minha_lista = []
quantidade_rep = random.randint(1, 2000)
for i in range(0, quantidade_rep):
    novo_valor_random = random.randint(1,50)
    minha_lista.append(novo_valor_random)

print(minha_lista)
print(minha_lista[len(minha_lista)-1])