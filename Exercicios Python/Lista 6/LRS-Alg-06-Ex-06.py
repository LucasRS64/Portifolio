def divisible(n) :
    listaN = []
    for x in range(1, n) :
     if n % x == 0 :
        listaN.append(x)
    x += 1
    return listaN

def main():
    n = int(input("Digite um numero inteiro positivo para ser dividido: "))
    lista_divisores = divisible(n)
    print(lista_divisores)
    
if __name__ == "__main__":
    main()