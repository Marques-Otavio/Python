# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~') #obtém o diretório Home do usuário atual
DESKTOP = os.path.join(HOME, 'Desktop') #cria o caminho até a Área de Trabalho (Desktop)
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Exemplo') #define a pasta de origem que será copiada
NOVA_PASTA = os.path.join(DESKTOP, 'Nova Pasta') #define a pasta de destino da cópia

# os.unlink(NOVA_PASTA) #apaga uma pasta vazia
shutil.rmtree(NOVA_PASTA, ignore_errors=True) # Apaga a pasta recursivamente(todo o caminho)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)