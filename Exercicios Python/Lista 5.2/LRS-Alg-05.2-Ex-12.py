def eh_valida(senha) :
    num = 0
    maisc = 0
    minu = 0
    if len(senha) < 8 :
       return False
    elif len(senha) >= 8 :
        for x in range(0, len(senha)) :
            if senha[x].isupper():
                maisc += 1
            if senha[x].isdigit():
                num += 1   
            if senha[x].islower():
                minu += 1
        if maisc >= 1 and num >= 1 and minu >= 1 :
            return True
        else :
            return False
def main():
  senha = input("Digite uma senha: ")
  print(eh_valida(senha))
if __name__ == "__main__":
    main()