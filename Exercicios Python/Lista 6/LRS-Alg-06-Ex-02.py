lista1 = []
while True :
    x = int(input("Digite os numeros para inserir na lista(digite 0 para finalizar):"))
    if x == 0 :
        break
    else :
        lista1.append(x)

lista1.sort(reverse=True)

print(lista1)