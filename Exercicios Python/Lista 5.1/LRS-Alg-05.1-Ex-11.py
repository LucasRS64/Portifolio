def conta_digitos(n, d) :
    first = 0
    second = 0
    resposta = 0
    first = str(n)
    second = str(d) 
    for x in range(len(first)) :
        if first[x] == second :
            resposta += 1
        x += 1
    return resposta
def eh_permutacao(n1, n2) :
    for i in range(10) :
        if (conta_digitos(n1, i) != conta_digitos(n2, i)) :
            return False
    return True

n1 = input("digite os elementos de a ")
n2 = input("digite os elementos de b ")

if eh_permutacao(n1, n2) :
    print("e permutacao")
else :
    print("nao e uma permutacao")
