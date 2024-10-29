def mediana(a, b, c) :
    maior = max(a,b,c)
    menor = min(a,b,c)
    meio = a + b + c - maior - menor
    return meio

def main():
    a = float(input("digite o valor de a: "))
    b = float(input("digite o valor de b: "))
    c = float(input("digite o valor de c: "))

    print(f"a media entre os valores e {mediana(a,b,c)}")
if __name__ == '__main__': 
    main()
