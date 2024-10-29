def frete(qtd_itens) :
    total = 0
    for x in range(0, qtd_itens) :
        if (x == 1) :
            total += 10.95
        else :
            total += 2.95
    return total

def main():

    qtd_itens = int(input("Quantidade de itens comprados: "))

    print(f"O custo de envio dos itens sera {frete(qtd_itens):.2f}")
if __name__ == '__main__': 
    main()



