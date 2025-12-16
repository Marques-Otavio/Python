"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#numero = input('Digite um numero inteiro ')

#if '.' or ',' in numero:
#   print('Isso nao e um numero inteiro')
#
#else: 
#   if (int(numero) % 2) == 1:
#       print('O numero digitado e impar ')
#
#   elif (int(numero) % 2) == 0:
#       print('O numero digitado e par ')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#horario = input('Que horas sao? ')
#horario = float(horario)

#if horario >= 0 and horario <= 11:
#    print('Bom dia!')

#elif horario >= 12 and horario <= 17:
#    print('Boa tarde!')

#elif horario >= 18 and horario <= 23:
#    print('Boa noite!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Informe o seu nome ')

if len(nome) <= 4:
    print('Seu nome e curto')

elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome e normal')

elif len(nome) > 6:
    print('Seu nome e muito grande')
    