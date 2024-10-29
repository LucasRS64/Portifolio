def decimal_para_binario(q):
    if q == 0:
        return "0"

    binario = ""
    
    while q > 0:
        resto = q % 2  
        binario = str(resto) + binario  
        q = q // 2  
    
    return binario

def main():
    try:
        numero_decimal = int(input("Digite um número decimal: "))
        resultado_binario = decimal_para_binario(numero_decimal)
        print(f"O número decimal {numero_decimal} em binário é: {resultado_binario}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()