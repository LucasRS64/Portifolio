def codificar_run_length(lista):
    lista_codificada = []

    def codificar_recursivo(index):
        if index >= len(lista):
            return lista_codificada
        contador = 1
        while index + contador < len(lista) and lista[index + contador] == lista[index]:
            contador += 1
        lista_codificada.append(lista[index])
        lista_codificada.append(contador)
        return codificar_recursivo(index + contador)

    return codificar_recursivo(0)

def main():
    string_usuario = input("Digite uma string: ")

    lista_codificada = codificar_run_length(string_usuario)

    print("String codificada em run-length:", lista_codificada)

if __name__ == "__main__":
    main()