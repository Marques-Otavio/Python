import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo = 10

    resultado = 0
    for digito in nove_digitos:
        resultado += (int(digito) * contador_regressivo)
        contador_regressivo -= 1

    primeiro_digito = resultado * 10 % 11 

    primeiro_digito = primeiro_digito if primeiro_digito <=9 else 0
    

    dez_digitos = nove_digitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    resultado_2 = 0

    for digito_2 in dez_digitos:
        resultado_2 += (int(digito_2) * contador_regressivo_2)
        contador_regressivo_2 -= 1

    segundo_digito = resultado_2 * 10 % 11

    segundo_digito = segundo_digito if segundo_digito <=9 else 0


    cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado_calculo)