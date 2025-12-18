"""
Iterando strings com while
"""
#       0123456789
nome = 'Otavio Augusto'  # Iteráveis
#      1110987654321

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1
    
print(novo_nome)
