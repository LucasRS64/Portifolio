#Centena, dezena, unidade. Dado um número de três algarismos N = CDU (onde C é o
#algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
#programa Python que receba do usuário o número inteiro N, e imprima separadamente a
#centena, a dezena e a unidade.

val = int(input("digite o valor: "))


c = val // 100
x = val % 100
d = x // 10
u = x % 10

print(f'centena : {c} *** dezena : {d} *** unidade : {u}')