import random

def criar_cartela():
    cartela = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}

    for letra in cartela:
        inicio_intervalo = 1 if letra == 'B' else 15 * (ord(letra) - ord('B'))
        fim_intervalo = inicio_intervalo + 14

        numeros_coluna = random.sample(range(inicio_intervalo, fim_intervalo + 1), 5)
        cartela[letra] = numeros_coluna

    return cartela

def exibir_cartela(cartela):
    print("Cartela de Bingo:")
    print(" B   I   N   G   O")
    for i in range(5):
        for letra in "BINGO":
            print(f"{cartela[letra][i]:2d}", end="  ")
        print()

def main():
    cartela = criar_cartela()

    exibir_cartela(cartela)

if __name__ == "__main__":
    main()