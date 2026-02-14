# isinstance - serve para saber se objeto e de determinado tipo 
lista = [
    'a', 1, 1.1, True, [0, 1, 2], 
    (1, 2), {0, 1}, {'nome': 'Otavio'}
]

for item in lista:
    if isinstance(item, set):
        print('Str')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('Str')
        print(item.upper(), isinstance(item, set))

    if isinstance(item, (int, float)):
        print('Num')
        print(item, item * 2)
    
    else:
        print('outro')
