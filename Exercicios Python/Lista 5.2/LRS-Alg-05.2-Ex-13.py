def dias_mes(ano,mes) :
    x = 0
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) :
        x += 1
        return x
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) :
        x += 2
        return x
    elif mes == 2 :
        if (ano % 400 == 0 or ano % 4 == 0) :
            x += 3
            return x
        else :
            x += 4
            return x
        

def main():
    mes = int(input("Digite um mes: "))
    ano = int(input("Digite um ano: "))
    if (dias_mes(ano,mes) == 1) :
        print("nesse mes possui 30 dias.")
    elif (dias_mes(ano,mes) == 2) :
        print("nesse mes possui 31 dias.")
    elif (dias_mes(ano,mes) == 3) :
        print("nesse mes possui 29 dias.")
    elif (dias_mes(ano,mes) == 4) :
        print("nesse mes possui 28 dias.")
if __name__ == "__main__":
    main()