def removeDuplicata(listaN, n) :
    lista_notDouble = []
    for x in listaN :
       if x not in lista_notDouble :
          lista_notDouble.append(x)
    return lista_notDouble 



def main():
    listaN = []
    while True :
     n = input("Digite palavras para inserir na lista(Enter sem nada para finalizar): ")
     n.upper
     if n == '' :
        break
     else :
        listaN.append(n)
    listaN_duplicatas_rm = removeDuplicata(listaN, n)
    print("Lista com duplicatas: ", listaN)
    print("Lista com duplicatas removidas:", listaN_duplicatas_rm)
if __name__ == "__main__":
    main()