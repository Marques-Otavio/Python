#1) Escreva um programa em que o usuário possa digitar diversos números (de 1 a 12) e 
#armazene esses números em uma lista. Após a lista de números inteiros estar completamente 
#preenchida, percorra com um segundo laço de repetição cada valor, e imprima o nome do mês 
#correspondente a cada número contido na lista.
lista = []
num = 1
while num >=1 and num <=12:
    num = int(input('Digite um numero de 1 a 12(ou outro para cancelar)' ))
    lista.append(num)

else:
    lista.pop()
    print(lista)

mes = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novenbro','Dezembro',]
for i in range (0,len(lista)):
    posicao = lista[i]
    print(mes[posicao - 1])



#2) Escreva um programa que leia 10 palavras usando um laço FOR, armazenando-as em uma 
#lista. Em seguida, crie um segundo laço de repetição para percorrer a lista e verificar qual é a 
#palavra que possui o maior número de caracteres. Por fim, imprima apenas a palavra com o 
#maior número de caracteres. 
lista = []
nomes = []
for i in range (10):
    nomes = str(input('Informe nomes:')) 
    lista.append(nomes)

maior = ''
for nomes in lista:
    if len(nomes) > len(maior):
        maior = nomes
print('O maior nome digitado foi:', maior)



#3)Faça um programa que leia 8 números inteiros e armazene uma lista. Em um segundo laço 
#de repetição, verifique cada valor e remova aqueles números que não são pares. Por fim, 
#imprima a lista com as modificações realizadas.  
lista = []
num = 1
for i in range (8):
    num = int(input("Informe um numero inteiro:"))
    lista.append(num)
print(lista)

lista2 = []
for i in range (len(lista)):
    if lista[i] % 2 == 0:
        lista2.append(lista[i])
print(lista2)



#4) Faça um programa que leia 10 idades e armazene em uma lista. Em um segundo laço, 
#percorra a lista e descubra a maior e a menor idade. Ao final, deve ser impresso todas as 
#idades, além da maior e menor idade. Veja o exemplo abaixo.
lista = []
for i in range (8):
    idade = int(input('Informe uma idade: '))
    lista.append(idade)

maior = lista[0]
menor = lista[0]
for idade in lista:
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
            
print(lista)
print('A maior idade digitada foi:',maior)
print('A menor idade digitada foi:',menor)

#5) Faça um Programa que leia 10 letras (minúsculas) e armazene em uma lista. Crie um segundo 
#laço de repetição para percorrer cada letra salva na lista, depois, imprima quantas consoantes 
#foram lidas (mesmo aquelas que sejam repetidas na lista).
lista = []
listavog = ['a','e','i','o','u']
contag_consoant = 0
consoantes = ''
for i in range (10): 
    letra_atual = input('Digite uma letra minuscula:')
    lista.append(letra_atual)
    if letra_atual not in listavog:
        contag_consoant += 1
        consoantes += letra_atual +''

print('A quantidade de consoantes e:', contag_consoant)
print('As consoantes digitadas foram:', consoantes)
