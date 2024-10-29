def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def main():
    try:
        a = int(input("Digite o primeiro número inteiro positivo: "))
        b = int(input("Digite o segundo número inteiro positivo: "))
        
        if a <= 0 or b <= 0:
            raise ValueError("Os números devem ser inteiros positivos.")
        
        resultado = mdc(a, b)
        print(f"O máximo divisor comum de {a} e {b} é: {resultado}")
    
    except ValueError as ve:
        print(f"Entrada inválida: {ve}")

if __name__ == "__main__":
    main()