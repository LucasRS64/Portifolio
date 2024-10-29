import math
x = float(input("digite o valor de x: "))
raiz = x/2
while math.fabs((raiz * raiz) - x) > 10**-12 :
    raiz = (raiz + (x/raiz)) /2
print(raiz)