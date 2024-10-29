b1 = float(input("quantos vasilhames de um litro ou menos? "))
b2 = float(input("quantos vasilhames de maior que 1 litro? "))

val_1l_menos = b1 * 0.10
val_superior = b2 * 0.25

val_total = val_1l_menos + val_superior


print(f' Valor total de creditos: R${val_total:.2f}')
