def organize(listaN, n) :
    lista_organizada = sorted(listaN)
    return lista_organizada

def main():
    listaN = []
    while True :
     n = input("Digite palavras para inserir na lista(Enter sem nada para finalizar): ")
     if n == '':
        break
     else :
        listaN.append(n)
    listaX = organize(listaN, n)
    print("Lista original: ", listaN)
    for x in listaX :
       print(x)
if __name__ == "__main__":
    main()