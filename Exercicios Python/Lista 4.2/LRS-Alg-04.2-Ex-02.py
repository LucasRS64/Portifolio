i = 0
val = 4.95
while i < 5:
    descont = val * 0.60
    val_final = val - descont
    print(f'valor inicial: {val:.2f} --->  valor do desconto(60%): {descont:.2f}  ---> valor com desconto: {val_final:.2f}')
    val = val + 5.00
    i += 1


