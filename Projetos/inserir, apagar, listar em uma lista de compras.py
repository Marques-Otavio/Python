import os


lista = []

while True:
    opcao = input('[i]nserir, [a]pagar, [l]istar ')


    if opcao == 'i':
        os.system('cls')
        item = input('Qual item deseja inserir? ')
        lista.append(item)



    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            if indice < 0 or indice >= len(lista):
                print('Indice fora do intervalo da lista')
            else:
                del lista[indice]
                print('Item removido com sucesso')
        except ValueError:
            print('por favor, digite um numero inteiro')
        except IndexError:
            print('Indice nao existe na lista')



    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nao ha nada para listar')
            
        for i, item in enumerate(lista):
            print(i, item)


    else:
        print('Escolha uma opcao valida')

