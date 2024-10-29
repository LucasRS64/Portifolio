import math
r = float(input("qual o valor do raio? "))

area = math.pi*math.pow(r, 2)

volume = 4 / 3 * math.pi*math.pow(r, 3)



print(f'o valor da area é {area:.2f}')
print(f'o valor do volume é {volume:.2f}')