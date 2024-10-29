def para_base_10(numero, base):
    numero = numero.upper()
    valor = 0
    expoente = len(numero) - 1
    for digito in numero:
        if digito.isdigit():
            valor += int(digito) * base ** expoente
        else:
            valor += (ord(digito) - 55) * base ** expoente
        expoente -= 1
    return valor

def de_base_10(numero, base):
    resultado = ""
    while numero > 0:
        resto = numero % base
        if resto < 10:
            resultado = str(resto) + resultado
        else:
            resultado = chr(resto + 55) + resultado
        numero //= base
    return resultado

def converter():
    base_origem = int(input("Digite a base de origem (2 a 16): "))
    base_destino = int(input("Digite a base de destino (2 a 16): "))
    numero = input("Digite o número a ser convertido: ")

    if base_origem < 2 or base_origem > 16 or base_destino < 2 or base_destino > 16:
        print("Bases inválidas.")
        return

    if base_origem == 10:
        numero_base_10 = int(numero)
    else:
        numero_base_10 = para_base_10(numero, base_origem)

    if base_destino == 10:
        resultado = str(numero_base_10)
    else:
        resultado = de_base_10(numero_base_10, base_destino)

    print("Resultado da conversão:", resultado)

def main():
    converter()
if __name__ == "__main__":
    main()