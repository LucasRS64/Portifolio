def encaixa(a, b) :
    first = 0
    second = 0
    first = str(a)
    second = str(b)
    for x in range(-1, 0) :
        if first[x] == second :
            return True 
        else :
            return False
    x += 1
a = int(input("um numero: "))
b = int(input("um digito para ver se encaixa: "))

if encaixa(a, b) :
    print("Encaixa!")
else :
    print("nao encaixa")
