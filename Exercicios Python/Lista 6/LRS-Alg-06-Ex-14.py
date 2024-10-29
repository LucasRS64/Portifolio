def precedencia(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático (+, -, *, /, ^): ")
    prec = precedencia(operador)
    if prec != -1:
        print(f"A precedência do operador {operador} é: {prec}")
    else:
        print("Erro: Entrada inválida. O operador não é reconhecido.")

if __name__ == "__main__":
    main()