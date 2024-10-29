n = int(input("digite um numero positivo: "))
a = 0
for x in range(0, n):
    form = (n-x)/(x+1)
    a = a + form
    print(a) 