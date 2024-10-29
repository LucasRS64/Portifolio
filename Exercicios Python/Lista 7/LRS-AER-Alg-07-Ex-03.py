def buscaReversa(dicionario, valor):
    chaves_encontradas = []
    for chave, v in dicionario.items():
        if v == valor:
            chaves_encontradas.append(chave)
    return chaves_encontradas

def main():    
    dicionario = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 2}

    valor = 2

    chaves_encontradas = buscaReversa(dicionario, valor)

    if chaves_encontradas:
        print(f"Chaves encontradas para o valor {valor}: {chaves_encontradas}")
    else:
        print(f"Nenhuma chave encontrada para o valor {valor}")

if __name__ == "__main__":
    main()