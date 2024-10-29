pi= 3
form = 0
a = 2
b = 3
c = 4
fin = 0
for x in range(1, 16) :
    if (x == 1) :
        print(pi)
    else :
            if (x == 2):
                form = pi + (4/(a*b*c))
                fin = fin + form 
                print(fin)
                a += 2
                b += 2
                c += 2
            if (x % 2 == 0 and x != 2):
                form = (4/(a*b*c))
                fin = fin + form 
                print(fin)
                a += 2
                b += 2
                c += 2
            else :
                form = (4/(a*b*c))
                fin = fin - form
                print(fin)
                a += 2
                b += 2
                c += 2
    x = x + 1
  