import random
def sorteia_dado() :
   var_1 = 0
   var_2 = 0
   var_3 = 0
   var_4 = 0
   var_5 = 0
   var_6 = 0
   numero_sorteios = 1000000
   for x in range (0,numero_sorteios) :
        x = random.randrange(1,7)
        if (x == 1) :
            var_1 += 1
        if (x == 2) :
            var_2 += 1
        if (x == 3) :
            var_3 += 1
        if (x == 4) :
            var_4 += 1
        if (x == 5) :
            var_5 += 1
        if (x == 6) :
            var_6 += 1
   chance_1 = (var_1 / numero_sorteios) * 100
   chance_2 = (var_2 / numero_sorteios) * 100
   chance_3 = (var_3 / numero_sorteios) * 100
   chance_4 = (var_4 / numero_sorteios) * 100
   chance_5 = (var_5 / numero_sorteios) * 100
   chance_6 = (var_6 / numero_sorteios) * 100
   if (chance_1 == chance_2 == chance_3 == chance_4 == chance_5 == chance_6) :
       return print(f'todas as probabilidades foram iguais!!!')
   if (chance_1 != chance_6) :
       return print(f'As probabilidades foram diferentes: \nporcentagem de 1: {chance_1:.3f}% \nporcentagem de 2: {chance_2:.3f}% \nporcentagem de 3: {chance_3:.3f}% \nporcentagem de 4: {chance_4:.3f}% \nporcentagem de 5: {chance_5:.3f}% \nporcentagem de 6: {chance_6:.3f}%')

sorteia_dado()