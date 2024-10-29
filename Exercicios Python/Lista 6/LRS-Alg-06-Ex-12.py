def verificar_ordem(lista):
    if all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1)):
        return "crescente"
    elif all(lista[i] >= lista[i + 1] for i in range(len(lista) - 1)):
        return "decrescente"
    else:
        return "não classificada"

def main():
    lista = input("Digite uma lista de números separados por espaço: ").split()
    lista = [int(num) for num in lista]  

    ordem = verificar_ordem(lista)
    if ordem != "não classificada":
        print(f"A lista está em ordem {ordem}.")
    else:
        print("A lista não está classificada.")

if __name__ == "__main__":
    main()