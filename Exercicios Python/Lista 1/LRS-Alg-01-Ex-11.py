import math
t1 = float(input("qual a latitude do ponto 1? "))
g1 = float(input("qual a longitude do ponto 1? "))
t2 = float(input("qual a latitude do ponto 2? "))
g2 = float(input("qual a longitude do ponto 2? "))

math.radians(t1)
math.radians(g1)
math.radians(t2)
math.radians(g2)

dist = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))

print(dist)
