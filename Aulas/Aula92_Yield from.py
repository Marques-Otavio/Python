# Yield from
#um monte de teste sem objetivo
def gen1():
    print('Comecou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')

def gen3():
    print('Comecou gen2')
    yield 10
    yield 20
    yield 30
    print('Acabou gen2')

def gen2(gen1 = None):
    print('Comecou gen3')
    if gen1 is not None:
        yield from gen1
    yield 4
    yield 5
    yield 6
    print('Acabou gen3')    

g1 = gen2(gen1)
g2 = gen2(gen3)
for num in g1:
    print(num)
for num in g2:
    print(num)