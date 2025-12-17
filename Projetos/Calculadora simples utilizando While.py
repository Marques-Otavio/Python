'''Calculadora com While'''
while True:
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operadores = input('Digite o operador (+-*/): ')

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    
    except:
        ...

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue

    operadores_permitidos = '+-/*'
    
    if operadores not in operadores_permitidos:
        print("operador invalido")    
        continue

    if len(operadores) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta, confira o resultado abaixo')
    if operadores == '+':
        soma = num1_float + num2_float
        print(f'A soma e {soma}')

    elif operadores == '-':
        sub = num1_float - num2_float
        print(f'A subtracao e {sub}')

    elif operadores == '*':
        mult = num1_float * num2_float
        print(f'A multiplicacao {mult}')

    elif operadores == '/':
        div = num1_float / num2_float
        print(f'A divisao {div}')


    sair = input('Voce quer sair? [S]im: ').lower().startswith('s')

    if sair is True:
        break
