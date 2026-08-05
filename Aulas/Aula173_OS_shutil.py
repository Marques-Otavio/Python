# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~') #obtém o diretório Home do usuário atual
DESKTOP = os.path.join(HOME, 'Desktop') #cria o caminho até a Área de Trabalho (Desktop)
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo') #define a pasta de origem que será copiada
NOVA_PASTA = os.path.join(DESKTOP, 'Nova Pasta') #define a pasta de destino da cópia

os.makedirs(NOVA_PASTA, exist_ok=True) #cria a pasta de destino, caso ela ainda não exista

for root, dirs, files in os.walk(PASTA_ORIGINAL): #percorre todas as pastas, subpastas e arquivos da pasta original

    for dir_ in dirs: #percorre todas as subpastas encontradas
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        ) #cria o caminho correspondente da subpasta no destino

        os.makedirs(caminho_novo_diretorio, exist_ok=True) #cria a subpasta no destino, se ela não existir

    for file in files: #percorre todos os arquivos da pasta atual
        caminho_arquivo = os.path.join(root, file) #monta o caminho completo do arquivo original
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        ) #monta o caminho completo onde o arquivo será copiado

        shutil.copy(caminho_arquivo, caminho_novo_arquivo) #copia o arquivo para a nova pasta, preservando o original