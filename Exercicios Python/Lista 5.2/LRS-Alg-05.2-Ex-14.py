def date_magic(ano,mes,dia) :
    if (dia * mes == (ano-1900)) :
        return True
    else :
        return False

def main():
    dia = int(input("Digite um dia: "))
    mes = int(input("Digite um mes: "))
    ano = int(input("Digite um ano: "))
    if (date_magic(ano,mes,dia) == 1) :
        print("E uma data magica!")
    else :
        print("nao e um data magica!")
if __name__ == "__main__":
    main()