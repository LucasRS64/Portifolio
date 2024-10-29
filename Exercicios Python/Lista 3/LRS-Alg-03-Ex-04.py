#Crie um programa Python que determina e exibe o nome de um polígono
#regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
#polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
#programa deve exibir uma mensagem de erro.

x = int(input("Quantos lados? "))


if (x < 3 or x > 10) :
    print("*****ERRO*****")
elif (x == 3) :
    print("Triângulo")
elif (x == 4) :
    print("Quadrado")
elif (x == 5) :
    print("Pentágono")
elif (x == 6) :
    print("Hexágono")
elif (x == 7) :
    print("Heptágono")
elif (x == 8) :
    print("Octógono")
elif (x == 9) :
    print("Eneágono")
elif (x == 10) :
    print("Decágono")