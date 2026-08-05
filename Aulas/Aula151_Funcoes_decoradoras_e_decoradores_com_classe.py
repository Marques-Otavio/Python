

def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


def adiciona_repr(cls): #gerando repr por composicao
    cls.__repr__ = meu_repr
    return cls
    
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

brasil = Time('Brasil')
argentina = Time('Argentina')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(argentina)
print(terra)
print(marte)
