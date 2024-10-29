def encaixa(a, b) :
    first = 0
    second = 0
    resposta = 0
    first = str(a)
    second = str(b)
    if first > second :
        for x in range(0, len(first)) :
            for y in range(0, len(second)) :
                if first[x] == second[y] :
                    resposta += 1
                y += 1
            x += 1
    elif second > first :
        for x in range(0, len(first)) :
            for y in range(0, len(second)) :
                if first[x] == second[y] :
                    resposta += 1
                y += 1
            x += 1
    return resposta

a = int(input("um numero: "))
b = int(input("outro numero: "))

x1 = str(a)
x2 = str(b)


if (encaixa(a, b) < len(x1)) and encaixa(a, b) == len((x2)) :
    print("b e segmento de a")
if (encaixa(a, b) > len(x1) and encaixa(a,b) < len(x2)) :
    print("a e segmento de b")
if (encaixa(a, b) < len(x1) and encaixa(a, b) < len(x2)) :
    print("um nao e segmento do outro")