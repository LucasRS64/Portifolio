#Desenvolva um programa que obtenha do usuário um
#número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
#fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).

val = int(input("digite o valor? "))


num1 = val // 1000
x = val % 1000
num2 = x // 100
x1 = x % 100
num3 = x1 // 10
num4 = x1 % 10

soma = num1 + num2 + num3 + num4

print(soma)