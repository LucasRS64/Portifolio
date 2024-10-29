c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

a1 = str(input("Nota musical: "))

a = a1.lower()

index1 = 0
index2 = 1

x2 = a[index1]
x = float(a[index2])

if (x2 == 'a') :
    freq = a4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'c') :
    freq = c4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'd') :
    freq = d4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'e') :
    freq = e4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'f') :
    freq = f4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'g') :
    freq = g4 / 2 ** (4 - x)
    print(f'{freq:.2f}')
elif (x2 == 'b') :
    freq = b4 / 2 ** (4 - x)
    print(f'{freq:.2f}')