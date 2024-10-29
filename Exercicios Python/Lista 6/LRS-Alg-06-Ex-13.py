def countRange(lista, minimo, maximo):
    contador = 0
    for elemento in lista:
        if minimo <= elemento < maximo:
            contador += 1
    return contador

def main():
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    minimo = 5
    maximo = 15

    quantidade = countRange(lista, minimo, maximo)
    print(f"Quantidade de elementos na lista entre {minimo} e {maximo}: {quantidade}")

if __name__ == "__main__":
    main()