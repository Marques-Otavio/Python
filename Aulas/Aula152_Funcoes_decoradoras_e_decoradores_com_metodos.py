

def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


def adiciona_repr(cls): #gerando repr por composicao
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
             return 'Voce esta em casa'
        return resultado
    return interno
# class MyReprMixin: # repr por heranca
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr


@adiciona_repr
class Time: #tirei a heranca para fazer com composicao
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
         return f'O planeta e {self.nome}'

brasil = Time('Brasil')
argentina = Time('Argentina')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(argentina)
print(terra.falar_nome())
print(marte.falar_nome())
