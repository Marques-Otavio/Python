# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1'))) #mostrando a conversao de classe do '1'->str para 1 ->int
print(float('1') + 1) #conversao de str para float e soma com int
print(bool(' ')) #String vazia considerada 'False' e com algum caractere considerada 'True'
print(str(11) + 'b') #concatenando (juntando) 11->int com 'b'->string, para isso convertemos o int em string