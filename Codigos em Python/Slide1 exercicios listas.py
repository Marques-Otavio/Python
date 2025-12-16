#1 

lista1 = [5, 6, 7, 8.8, 5, 6, 7.8, 9.8, 7]
print(lista1)
soma = sum(lista1)
media = soma / len(lista1)

print('A soma e:', "%.2f", soma)
print('A media e:', "%.2f", media)

#2
lista = []
nomes = 1
while nomes != '-1':
    nomes = str(input("Informe nomes (caso queira parar, informa -1): "))
    lista.append(nomes)

else:
    lista.pop()
    print(lista)

#3
lista = []
num = 0
while num >= 0 and num < 99999999999999999999999999999999:
    num = int(input('Digite um numero inteiro positivo (ou -1 para cancelar)'))
    lista.append(num)

else:
    lista.pop()
    print(lista)

for i in range(0, len(lista)):
    if num <30:
        lista.remove(i)
        print(lista[i])

    

