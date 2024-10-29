letra = str(input("letra da posição: "))
num = int(input("numero da posição: "))

if (letra == 'a' or letra == 'c' or letra == 'e' or letra == 'g') :
    if (num % 2 == 0) :
        print("Quadrado Branco")
    else :
        print("Quadrado Preto")
else :
   
   if (num % 2 == 0) :
        print("Quadrado Preto")
   else :
       print("Quadrado Branco")
