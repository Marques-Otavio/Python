
    

   
matriz = []

for z in range(26):
    linha = []

    for y in range(65,90):
                
        number = 65 + (y+z)%26
                
        linha.append(chr(_(number)_))

    matriz.append(linha)





palavrachavestart = input()

N = int(input())
if(len(palavrachavestart) > 2 and len(palavrachavestart)<= 45 and N>0 and N<=150):



    for i in range (N):
        msg = input()

    
        size_chave = len(palavrachavestart)

        palavrachave = ''
        cont = 0





    for i in range(repeticao):
        palavrachave += palavrachave
    print(msg)
    print(palavrachave)





    for p in range(len(msg)):
        if(ord(msg[p])>=97 and ord(msg[p])<=122):
            palavrachave = palavrachave + palavrachavestart[cont&size_chave]
            cont += 1
        else:
            palavrachave = palavrachave + msg[p]

    print(palavrachave)

    crypto_mens = ''






    for j in range(len(msg)):

        linha = ord(palavrachave[j])-97
        coluna = ord(msg[j])-97

        if(linha >=0 and linha <26 and coluna >= 0 and coluna <26):
            #print('Matriz[',linha, ']-->[',coluna, ']-->', matriz[linha][coluna])
            crypto_mens += matriz[linha][coluna]
        else:
            #print('Matriz[',linha, ']-->[',coluna, ']-->', msg[j])
            crypto_mens += msg[j]

    print (crypto_mens)

        print('Matriz[',linha, ']-->[',coluna)

