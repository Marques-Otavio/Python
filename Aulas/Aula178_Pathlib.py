# usamos a pathlib para trabalhar com caminhos, 
# pastas e arquivos, de forma que um codigo
# funcioneem Windows, Linux e Mac
# Pathlib lê, detecta e corrige para a plataforma utilizada

from pathlib import Path


caminho_projeto = Path()
# print(caminho_projeto.absolute()) # absolute para pegar o caminho completo, se nao ele imprimiria '.', nesse caso

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

# print(caminho_arquivo.parent.parent) # parent busca a pasta mãe deste arquivo, portanto 2 .parent busca o parent do parent

ideias = caminho_arquivo.parent / 'ideias' # / junta dois arquivos para montar um novo caminho
print(ideias / 'arquivo.txt')

print(Path.home() / 'Desktop')# pega a home e junta com o Desktop para criar algo no proprio desktop

# Até aqui ele só gera caminhos, mas não cria nada

caminho_arquivo = Path.home() / 'Desktop' / 'Arquivo.txt'
# caminho_arquivo.touch() # .touch() faz o arquivo ser criado
# print(arquivo)
# caminho_arquivo.write_text('Olá Mundo') #escrever dentro do arquivo
# print(caminho_arquivo.read_text()) #ler o que há no arquivo
# caminho_arquivo.unlink() # unlink apaga o arquivo

caminho_arquivo.write_text('') # metodo simples para zerar o que tiver dentro do arquivo, sem exclui-lo, pois, .write sobrepoe a linha anterior

'''
abaixo, um metodo para escrever em varias partes do arquivo,
  pois com o primeiro exemplo, só fica disponível a ultima
  linha executada, ela meio que substitui a anterior
'''
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha \n')
#     file.write('Outra linha \n')

# print(caminho_arquivo.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True) # mkdir - cria um diretório (ao executar duas vezes, dará erro de arquivo ja existir, por isso exist_ok)

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Hey')

# caminho_pasta.rmdir() # rmdir - apaga a pasta

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.is_file():... #retorna se é arquivo (Boolean)
    if file.is_dir():... #retorna se é um dirtório (Boolean)
    if file.exists(): #retorna se o arquivo existe
        file.unlink()
    else:
        file.touch()

with file.open('a+') as text_file: #abre o arquivo para leitura e escrita, criando-o caso não exista e posicionando o cursor no final
    text_file.write('Olá mundo\n') #escreve "Olá mundo" seguido de uma quebra de linha
    text_file.write(f'file_{i}.txt') #escreve o nome do arquivo utilizando o valor da variável i

def rmtree(root: Path, remove_root=True): #remove recursivamente uma pasta e todo o seu conteúdo
    for file in root.glob('*'): #percorre todos os arquivos e subpastas do diretório
        if file.is_dir(): #verifica se o item atual é uma pasta
            print('DIR: ', file) #exibe o caminho da pasta encontrada
            rmtree(file, False) #remove recursivamente o conteúdo da subpasta
            file.rmdir() #remove a subpasta vazia
        else:
            print('FILE: ', file) #exibe o caminho do arquivo encontrado
            file.unlink() #remove o arquivo

    if remove_root: #verifica se a pasta principal também deve ser removida
        root.rmdir() #remove a pasta raiz após ela estar vazia