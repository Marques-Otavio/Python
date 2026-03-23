#Count iterador sem fim

'''
parecido com o range, porem o range tem fim e nao e iterador.
o count e usado quando precisa de um contador e nao sabe o fim

para utiliza-lo deve-se importar o itertools, pois ele nao esta no python base, e sim la
'''

from itertools import count

c1 = count()
r1 = range(100)

print('count')
for i in c1: #o count cria um loop infinito
    if c1 >= 100: # por esse motivo coloca essa condicao, que fara ele parar em certo numero
        break
    print(i) #imprime o numero

print()#somente para pular uma linha no terminal

print('range')
for i in r1: # ja o range precisa do fim estabelecido (esta la na criacao da variavel)
    print(i) # portanto nao e necessario um break


c2 = count(10) # no count so e possivel passar o valor de inicio, nesse caso ele iria comecar do 10
r2 = range(10, 100) # ja no range e obrigatorio passar o valor de termino, e o valor de inicio e opcional


r3 = range(10, 100, 5) #inicio, fim, e o terceiro valor representa o step, ou seja, ele vai percorrer do 10 ao 100, pulando de 5 em 5
c3 = count(10, 5) #inicio, step -> loop continua infinito porem de 5 em 5
