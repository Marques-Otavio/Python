# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence): #criando uma lista que funciona igual a padrao
    def __init__(self):
        self._data = {}
        self._index = 0 #indice atual
        self._next_index = 0 #proximo indice

    def append(self, *values): #adiciona novos valores no final
        ''' 
        aqui no append, normalmente nao aceita dois valores de uma vez, 
        porem com essa mudanca de encapsulamento, posso colocar varios valores para um append
        '''
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int: #confere o tamanho da lista
        return self._index

    def __getitem__(self, index): #pega o valor do indice escolhido
        return self._data[index]

    def __setitem__(self, index, value): #coloca (seta) o valor no indice escolhido
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self): #retorna o proximo indice (se houver)
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Otavio')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')