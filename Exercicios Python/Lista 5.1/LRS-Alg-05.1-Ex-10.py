n = int(input("digite o valor de n "))
d = int(input("digite o valor de d "))
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

if (d>0 and d<=9) :
        print(f"o digito {d} foi encontrado {conta_digitos(n, d)} vez(es)")
else :
        print("d e invalido")

    
    