def decodificar_run_length(lista_codificada):
    lista_descompactada = []

    def decodificar_recursivo(index):
        if index >= len(lista_codificada):
            return lista_descompactada
        if isinstance(lista_codificada[index], int):
            for _ in range(lista_codificada[index]):
                lista_descompactada.append(lista_codificada[index - 1])
            return decodificar_recursivo(index + 1)
        else:
            lista_descompactada.append(lista_codificada[index])
            return decodificar_recursivo(index + 1)

    return decodificar_recursivo(0)

def main():
    lista_codificada = ["A", 12, "B", 4, "A", 6, "B", 1]
    print("Lista codificada em run-length:", lista_codificada)

    lista_descompactada = decodificar_run_length(lista_codificada)
    print("Lista descompactada:", lista_descompactada)

if __name__ == "__main__":
    main()