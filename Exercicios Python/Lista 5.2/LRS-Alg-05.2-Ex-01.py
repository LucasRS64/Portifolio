import math
def hipotenusa(a, b) :
    hip = 0
    cat = (math.pow(a, 2) + math.pow(b, 2))
    hip = math.sqrt(cat)
    return hip
 
def main():

    a = float(input("Primeiro lado menor do triangulo: "))
    b = float(input("segundo lado menor do triangulo: "))
    print(f"a hiputenusa:{hipotenusa(a, b)}")
if __name__ == '__main__': 
    main()