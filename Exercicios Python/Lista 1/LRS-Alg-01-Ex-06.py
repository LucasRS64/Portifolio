alm1 = float(input("Quanto foi o valor do prato principal? " ))
alm2 = float(input("Quanto foi o valor do suco? " ))
alm3 = float(input("Quanto foi o valor da sobremesa? " ))

tax_service = 0.10

total = alm1 + alm2 + alm3 * tax_service



print(f'R${total:.2f}')
