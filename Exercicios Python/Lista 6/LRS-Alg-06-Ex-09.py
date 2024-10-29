def obter_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou deixe em branco para parar): ")
        if entrada == "":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    return numeros

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    print("Digite números. Deixe em branco para parar.")
    numeros = obter_numeros()

    media = calcular_media(numeros)
    print(f"A média dos números digitados é: {media}")

    abaixo_da_media = [num for num in numeros if num < media]
    media_igual = [num for num in numeros if num == media]
    acima_da_media = [num for num in numeros if num > media]

    print("Valores abaixo da média:")
    print(abaixo_da_media)

    print("Valores médios:")
    print(media_igual)

    print("Valores acima da média:")
    print(acima_da_media)

if __name__ == "__main__":
    main()