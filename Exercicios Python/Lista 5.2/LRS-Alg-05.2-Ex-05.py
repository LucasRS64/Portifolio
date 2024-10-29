def ordinal(numero) :
    if (numero < 1 and numero > 12) :
        return  False
    else :
        if numero == 1 :
            return "Primeiro"
        elif numero == 2 :
            return "Segundo"
        elif numero == 3: 
            return "Terceiro"
        elif numero == 4 :
            return "Quarto"
        elif numero == 5 :
            return "Quinto"
        elif numero == 6: 
            return "Sexto"
        elif numero == 7 :
            return "Setimo"
        elif numero == 8 :
            return "Oitavo"
        elif numero == 9: 
            return "Nono"
        elif numero == 10 :
            return "Decimo"
        elif numero == 11 :
            return "Decimo-Primero"
        elif numero == 12: 
            return "Decimo-Segundo"
def main():
    numero = int(input("digite um valor entre 1 e 12: "))
    if ordinal(numero) :
        print(f"o numero em ordinal e  + {ordinal(numero)}")
    else : 
        print("")
if __name__ == '__main__': 
    main()
