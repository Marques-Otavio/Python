primeiro_valor = input('Digite um valor ')
segundo_valor = input('Digite outro valor ')

if primeiro_valor > segundo_valor:
    print('{0} e maior que {1}'.format(primeiro_valor, segundo_valor))

elif segundo_valor > primeiro_valor:
    print('{1} e maior que {0}'.format(primeiro_valor, segundo_valor))