mes = int(input("Mes: "))
dia = int(input("Dia: "))


if (mes == 1 and dia == 1) :
    print("Feriado: Confraternização universal!")
elif (mes == 4 and dia == 21) :
    print("Feriado: Tiradentes!")
elif (mes == 5 and dia == 1) :
    print("Feriado: Dia do trabalho!")
elif (mes == 9 and dia == 7) :
    print("Feriado: Dia da Independencia!")
elif (mes == 10 and dia == 12) :
    print("Feriado: Nossa Senhora Aparecida")
elif (mes == 11 and dia == 2) :
    print("Feriado: Finados!")
elif (mes == 11 and dia == 15) :
    print("Feriado: Proclamação da República")
elif (mes == 12 and dia == 25) :
    print("Feriado: Natal!")
else :
    print("Não é um feriado nacional.")