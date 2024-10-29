ano = int(input("Qual o ano? "))

if (ano % 400 == 0 or ano % 4 == 0) :
    print("o ano é bissexto!")
else :
    print("não é bissexto!")