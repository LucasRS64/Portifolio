import math
a = int(input("diga o valor de a "))
b = int(input("diga o valor de b "))
c = int(input("diga o valor de c "))

disc = b * b - 4 * a * c
sqrt = math.sqrt(abs(disc))

if (disc < 0) :
    print("equação com raizes não reais")
    print(-b / (2 * a), " + i", sqrt)
    print(-b / (2 * a), " - i", sqrt)
elif (disc == 0) : 
    print("real e a mesma raiz")
    print(-b / (2 * a))
else :
    print("real e duas diferentes raizes")
    print((-b + sqrt)/(2*a))
    print((-b - sqrt)/(2*a))
