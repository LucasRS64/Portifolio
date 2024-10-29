def digit() :
    digitos = 0
    n = int(input("digite um valor maior que zero: "))
    r = str(n)
    for x in range (len(r)) :
        digitos += 1
    return print(f'o numero de digitos e {digitos}')

digit()
