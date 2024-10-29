n = int(input("digite um numero positivo: "))
x = 1
i = 0
bx = 0
cx = 0
while i < n:
    if (x % 2 == 0):
       form = 1/x
       cx = cx + form 
       a = cx
       print(a)
    else :
        form = 1/x
        bx = bx + form
        a = bx
        print(a)
    x = x + 1
    i += 1
    bx = 0
    cx = 0