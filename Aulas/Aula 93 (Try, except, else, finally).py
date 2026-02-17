# Try, except, else e finally

# try:
#     a = 18
#     b = 0
#     c = a / b

# except:
#     ...
# print('Continuar')

# ESSE CODIGO ACIMA NAO E UMA BOA PRATICA,
# POIS ESCONDE POSSIVEIS ERROS, 
# TORNANDO-OS DIFICEIS DE SEREM IDENTIFICADOS



try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1' [100000])
    c = a / b

except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)

except NameError:
    print('Nome nao foi definido.')

except (TypeError, IndexError) as error: #colocando dois erros no mesmo except e adicionando-os em uma variavel...
    #( 'as' serve para indicar em qual variavel esta a instancia do erro)
    print('TypeError + IndexError') #print basico
    print('MSG:', error) #mostrando a mensagem do erro (string index out of range)
    print('Nome:', error.__class__.__name__) #mostrando o nome/classe do erro

except Exception:
    print('Erro desconhecido.')






