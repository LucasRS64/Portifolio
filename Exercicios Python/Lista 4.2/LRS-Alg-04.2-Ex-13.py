fator = 2
n = int(input("digite um numero inteiro (maior ou igual a 2): "))
while fator <= n :
    if (n < 2) :
        print("ERRO: Numero menor que 2")
        break
    elif (n % fator == 0) :
        n = n//fator
        print(fator)
    else :
        fator += 1