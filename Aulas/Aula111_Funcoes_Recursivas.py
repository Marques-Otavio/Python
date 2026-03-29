# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

'''
    FUNCOES RECURSIVAS NAO SAO MUITO USUAIS POIS TEM A MESMA FUNCAO DOS LACOS FOR E WHILE
'''
def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    # Caso base
    if inicio >= fim: #entao a funcao so retornara valor por causa dessa condicional
        return fim
    
    # Caso recursivo
    # contar até chegar ao final
    inicio += 1 # a funcao executa essa linha, vai pra debaixo

    return recursiva(inicio, fim)# ai essa linha retorna a propria funcao, 
        # chamando ela de novo, e nao devolvendo o resultado imediatamente, ou seja, 
        # ela entra e executa as linhas acima novamente

print(recursiva())



def fatorial (n):
    if n <= 1:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(5))