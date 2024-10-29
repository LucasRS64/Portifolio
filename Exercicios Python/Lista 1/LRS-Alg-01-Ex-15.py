import math
l = float(input("qual o valor de l? "))
n = float(input("qual o valor de n? "))

area = n * math.pow(l, 2) / 4 * math.tan(math.pi/n)

print(area)