# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicar(*args):
    total = 0
    for numero in args:
        total = numero * numero
        
    return total

resultado = multiplicar(1,2,3,4,5)
print(resultado)



# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    verifica = int(numero) % 2 == 0
    if verifica:
        return f'o {numero} e par'
        
    return f'o {numero} e impar'
    
print(par_impar(input('Digite um numero: ')))
