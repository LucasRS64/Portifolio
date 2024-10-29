n = int(input("digite o valor: "))


c = n // 100
x = n % 100
d = x // 10
u = x % 10

m = u * 100 + d * 10 + c

print(m)