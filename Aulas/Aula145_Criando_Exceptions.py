# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...

class OtherError():
    ...


def levantar():
    exception_ = MyError('A mensagem do meu erro')
    exception_.add_note('Olha a nota 1') # adicionando notas
    exception_.add_note('voce errou isso')
    raise exception_
try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OtherError('Vou lancar de novo')
    exception_.__notes__ += error.__notes__.copy() # para copiar as notas de cima
    exception_.add_note('Mais uma nota')
    raise exception_ from error