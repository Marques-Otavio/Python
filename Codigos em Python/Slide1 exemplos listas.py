#Adicionar numero na lista com laco de repeticao
lista1 = []                                                          
#lista vazia
for i in range (0,5):                                               

    num = float(input('Digite um numero para adicionar a lista: ')) 
    lista1.append (num)                                              
print(lista1)                                                        

print(lista1 [3:])                                                   

lista2 = [45.7, 53.5, 8.7, -10.3]                                   
concat = lista1 + lista2                                             
print (concat)                                                      


lista3 = [10, 3.5, 7, 10, 4]
print(lista3)
lista3.remove (10)
print(lista3)
#result: removeu apenas o primeiro "10"


lista3 = [10, 3.5, 7, 10, 4]
print(len(lista3)) 
#indica o numero de elementos da lista

lista3 = [10, 3.5, 7, 10, 4]
lista3.pop(3) 
#remove o item 3 da lista (comeca a contar em 0)
print(lista3)
print(len(lista3)) 
#indica o novo numero de elementos da lista

nome_lista = [10,20,30,40,50]
for i in range(0, len(nome_lista)):
    print(nome_lista[i])
#repetiu todos os itens da lista









