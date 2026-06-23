# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Otavio', 19)
p2  = Pessoa('Geni', 47)
p3 = Pessoa('Daniel', 45)
dados = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
            print('Fazendo Dump')
            dados = json.dump(dados, arquivo, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    print('Esse e o main')
    fazer_dump()