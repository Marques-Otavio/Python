lista1 = []

maior_palavra = ""
maior = 0
menor = 0
menor_palavra = ""
for i in range(0,10):
    palavra = (input("Informe uma palavra: "))



for i in range(0, len(lista1)):
    if len(lista1[i])>maior:
        maior = len(lista1[i])
        maior_palavra = lista1[i]

    if len(lista1[i])>menor:
        menor = len(lista1[i])
        menor_palavra = lista1[i]

print("A maior palavra é: ", maior_palavra)
print("A menor palavra é: ", menor_palavra)
