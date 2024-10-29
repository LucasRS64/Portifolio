def int2hex(num1) :
    y = str(num1)
    x = ''
    if num1 >= 0 and num1 <= 9 :
        return x + y
    else :
        if num1 == 10 :
            return 'A'
        elif num1 == 11 :
            return 'B'
        elif num1 == 12 :
            return 'C'
        elif num1 == 13 :
            return 'D'
        elif num1 == 14 :
            return 'E'
        elif num1 == 15 :
            return 'F'
def hex2int(num2) :
    num2 = num2.upper()
    if num2.isdigit():
        return int(num2)
    else:
        return ord(num2) - 55 if ord(num2) > 64 else None

def main():
    num2 = input("Digite um numero hexadecimal: ")
    num1 = int(input("Digite um numero base 10: "))

    print(f"de numero hexadecimal para decimal: {hex2int(num2)}")
    print(f"de numero decimal para hexadecimal: {int2hex(num1)}")
if __name__ == "__main__":
    main()