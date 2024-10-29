pessoa = 0
valor_total = 0
while True:
    r = input("Digite a idade da pessoa: ")
    if r == "":
        break
    pessoa = int(r)
    if (pessoa <= 12 and pessoa > 2) :
        valor_total += 14
    if (pessoa >= 65) :
        valor_total += 18
    if (pessoa > 12 and pessoa < 65) :
        valor_total += 23

print(f'O valor total a pagar e {valor_total:.2f}')