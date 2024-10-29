def triangulo_vdd(can1,can2,can3) :
    if (can1 >= can2 + can3 or can2 >= can1 + can3 or can3 >= can1 + can2) :
        return False
    else :
        return True
def main():
    can1 = float(input("diga o comprimento do canudo 1: "))
    can2 = float(input("diga o comprimento do canudo 2: "))
    can3 = float(input("diga o comprimento do canudo 3: "))
    print(triangulo_vdd(can1,can2,can3))
if __name__ == '__main__': 
    main()