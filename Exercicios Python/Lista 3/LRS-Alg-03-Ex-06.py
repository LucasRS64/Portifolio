#Baseado nos comprimentos dos seus lados, um triângulo pode ser
#classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
#apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
#programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
#uma mensagem informando qual é o tipo do triângulo.

x1 = float(input("Lado 1: "))
x2 = float(input("Lado 2: "))
x3 = float(input("Lado 3: "))

if (x1 == x2 and x1 == x3) :
    print("Equilátero")
elif (x1 == x2 and x1 != x3 or x2 == x3 and x3 != x1 or x1 == x3 and x2 != x1) :
    print("Isóceles")
else : 
    print("Escaleno")