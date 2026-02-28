
# Exercício - Adiando execução de funções

# Problema


# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, *args):
#     return funcao(*args)


# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)



#Solucao

def soma(x, y):

    return x + y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)

print(soma_com_cinco(10))


# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar=''):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna


# c = concatenar('a')
# print(c('b'))
# print(c('c'))
# print(c('d'))
# final = c()
# print(final)