def alinhamento(string_original, espacamento) :
    string_modificado = ""
    pulos = (espacamento - len(string_original)) // 2 
    for x in range(0, pulos) :
        string_modificado += "x" 
    return string_modificado + string_original
def main():
    string_original = input("Escreva uma string: ")
    espacamento = int(input("coloque a linha para centralizacao: "))
    print(alinhamento(string_original, espacamento))
if __name__ == '__main__': 
    main()
