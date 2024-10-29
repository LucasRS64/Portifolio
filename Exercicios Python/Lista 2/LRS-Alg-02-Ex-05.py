#Considere o software que controla uma máquina automática de compras.
#Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
#este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
#uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
#0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
#compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
#possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.



val = int(input("qual valor? "))

moe50 = val // 50
x = val % 50
moe25 =  x // 25 
x1 = x % 25
moe10 = x1 // 10
x2 = x1 % 10
moe5 = x2 // 5
x3 = x2 % 5
moe1 = x3

print(f'moedas de 50: {moe50} **** moedas de 25: {moe25} **** moedas de 10: **** {moe10} moedas de 5: **** {moe5} moedas de 1: **** {moe1} ')

