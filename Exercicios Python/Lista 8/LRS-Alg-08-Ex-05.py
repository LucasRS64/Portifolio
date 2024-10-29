def soma_recursiva():
    entrada = input("Digite um valor numérico (ou deixe em branco para finalizar): ")
    
    if entrada == "":
        return 0.0
    
    try:
        numero = float(entrada)
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        return soma_recursiva()  
    
    return numero + soma_recursiva()

def main():
    soma_total = soma_recursiva()
    print(f"A soma total dos valores inseridos é: {soma_total}")

if __name__ == "__main__":
    main()