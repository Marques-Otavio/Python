# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho = os.path.join('\\Users', 'DELL', 'Documents', 'UDEMY', 'Exemplo') #cria o caminho completo até a pasta "Exemplo"

counter = count() #cria um contador infinito começando em 0

for root, dirs, files in os.walk(caminho): #percorre todas as pastas, subpastas e arquivos do diretório
    the_counter = next(counter) #obtém o próximo valor do contador para identificar cada pasta percorrida

    print(the_counter, 'Pasta Atual', root) #exibe o número da iteração e o caminho da pasta atual

    for dir_ in dirs: #percorre todas as subpastas da pasta atual
        print('  ', the_counter, 'Dir', dir_) #exibe o nome de cada subpasta

    for file_ in files: #percorre todos os arquivos da pasta atual
        caminho_completo_arquivo = os.path.join(root, file_) #cria o caminho completo do arquivo
        print('  ', the_counter, 'File', caminho_completo_arquivo) #exibe o caminho completo de cada arquivo