num1 = int(input("digite um numero positivo: "))
num2 = int(input("digite outro numero positivo: "))
num3 = int(input("digite outro numero positivo: "))

maior = max(num1,num2,num3)
menor = min(num1,num2,num3)
meio = num1 + num2 + num3 - maior - menor

print(maior)
print(meio)
print(menor)