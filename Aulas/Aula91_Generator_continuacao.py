#
# generator = (n for n in range(60):)

# def generator(n=0):
#     yield 1 # pausar
#     print('continuando...')
#     yield 2 # pausar
#     print('Mais uma...')
#     yield 3 # pausar
#     return 'ACABOU'

# gen = generator(n=0)
# for n in gen:
#     print(n)

def generator(n=0, maximo = 10):
    while True:
        yield n 
        n += 1

        if n >= maximo:
            return

gen = generator(maximo = 60)
for n in gen:
    print(n)




