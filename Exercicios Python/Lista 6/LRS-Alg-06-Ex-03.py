def remove(listaN, n) :
    if len(listaN) < 4:
        raise ValueError("A lista deve conter pelo menos 4 valores.")
    
    
    sorted_list = sorted(listaN)
    
    
    trimmed_list = sorted_list[n:-n]
    
    return trimmed_list

def main():
    listaN = []
    while True :
     n = int(input("Digite os numeros para inserir na lista(Enter sem nada para finalizar): "))
     if n == None :
        break
     else :
        listaN.append(n)
    trimmed_list = remove(listaN, 2)
    print("Lista com extremos removidos:", trimmed_list)
if __name__ == "__main__":
    main()