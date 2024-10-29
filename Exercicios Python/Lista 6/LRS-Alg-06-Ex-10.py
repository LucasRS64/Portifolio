def formatar_lista(lista):
    tamanho = len(lista)
    if tamanho == 0:
        return ""
    elif tamanho == 1:
        return lista[0]
    elif tamanho == 2:
        return f"{lista[0]} e {lista[1]}"
    else:
        itens_formatados = ", ".join(lista[:-1])
        return f"{itens_formatados} e {lista[-1]}"

def main():
    listas = [
        [],
        ["maçãs"],
        ["maçãs", "laranjas"],
        ["maçãs", "laranjas", "bananas"],
        ["maçãs", "laranjas", "bananas", "limões"]
    ]

    for lista in listas:
        print(formatar_lista(lista))

if __name__ == "__main__":
    main()