import math
x0 = float(input("Digite a coordenada x de um ponto: "))
y0 = float(input("Digite a coordenada y de um ponto: "))
x1 = x0
y1 = y0
perimetro = 0
while True:
    r = input("Digite a coordenada x de um ponto(enter para sair): ")
    if r == "":
        break
    x2 = float(r)
    y2 = float(input("Digite a coordenada y de um ponto: "))
    
    # distancia de panterior ate patual
    distance = math.sqrt(pow((y2 - y1), 2) + pow((x2 - x1), 2))
    perimetro = perimetro + distance
    x1 = x2
    y1 = y2

perimetro = perimetro + math.sqrt(pow((y2 - y0), 2) + pow((x2 - x0), 2))

print(f"O perimetro deste poligono e igual a {perimetro}")
    
    