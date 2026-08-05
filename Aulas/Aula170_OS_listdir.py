# os.listdir para navegar em caminhos
# C:\Users\otavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\otavio\\Desktop\\EXEMPLO'

import os

caminho = os.path.join('\\Users', 'DELL', 'Documents', 'UDEMY', 'Exemplo') #cria o caminho completo até a pasta "Exemplo"

for pasta in os.listdir(caminho): #lista todos os arquivos e pastas que existem dentro de "Exemplo"
    caminho_completo_pasta = os.path.join(caminho, pasta) #cria o caminho completo para cada item encontrado

    if not os.path.isdir(caminho_completo_pasta): #verifica se o item é uma pasta
        continue #se não for uma pasta, pula para o próximo item

    for imagem in os.listdir(caminho_completo_pasta): #lista todos os arquivos existentes dentro da pasta encontrada
        print(imagem) #exibe o nome de cada arquivo (imagem) no terminal

