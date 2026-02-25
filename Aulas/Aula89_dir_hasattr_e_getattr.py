#dir - lista todos os atributos e métodos disponíveis do objeto
#hasattr - retorna True se o objeto possui esse atributo/método
#getattr - obtém o atributo pelo nome (string); se não existir, retorna valor_padrao (ou levanta erro se não for passado)
string = 'Otavio'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao existe o metodo', metodo)