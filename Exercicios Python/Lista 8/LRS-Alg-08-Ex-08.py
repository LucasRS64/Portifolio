def decimal_para_binario_recursivo(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_para_binario_recursivo(n // 2) + str(n % 2)

def main():
    try:
        numero_decimal = int(input("Digite um número decimal não negativo: "))
        if numero_decimal < 0:
            raise ValueError("O número deve ser não negativo.")
        resultado_binario = decimal_para_binario_recursivo(numero_decimal)
        print(f"O número decimal {numero_decimal} em binário é: {resultado_binario}")
    except ValueError as ve:
        print(f"Entrada inválida: {ve}")

if __name__ == "__main__":
    main()