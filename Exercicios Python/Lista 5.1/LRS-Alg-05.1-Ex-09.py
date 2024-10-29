ano = int(input("qual o ano? "))
def eh_bissexto(ano) :
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0) :
        return print("ano e bissexto.")
    else :
        return print("nao e bissexto.")
    
eh_bissexto(ano)