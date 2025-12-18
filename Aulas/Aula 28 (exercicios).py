"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Informe sua idade: ')
espaco = (' ')

if nome and idade:
    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nome[::-1]}')

    #nao precisava declarar variavel, somente: if ' ' in nome: 
    if espaco in nome:
        print('Seu nome contem espacos')
    else:
        print('Seu nome nao contem espacos')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome [-1]}')
else:
    print('Desculpe, voce deixou campos vazios')