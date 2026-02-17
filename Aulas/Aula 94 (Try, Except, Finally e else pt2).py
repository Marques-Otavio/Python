
try:
    print('ABRIR O ARQUIVO')
    8/0

except ZeroDivisionError as e: #tratar excessao (erro)
    print(e.__class__.__name__) #pegar nome do erro
    print(e) #pegar mensagem do erro

except IndexError as error: #capturando erro utilizando o 'as' e uma variavel 'error'
    print('IndexError')

except (NameError, IndentationError): #duas excessoes no mesmo except
    print('NameError, IndentationError')

else: #executado caso o codigo nao de erro (pouquissimo utilizado)
    print('Nao deu erro')

finally: #sempre sera executado mesmo se ocorrer um erro.
    print('FECHAR ARQUIVO')

