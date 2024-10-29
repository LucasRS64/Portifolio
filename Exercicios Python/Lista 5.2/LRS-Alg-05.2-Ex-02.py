def taximetro(distance, valor_inicial, taxa_var) :
    form = valor_inicial + (taxa_var * + ((distance * 1000) // 140))
    return form
def main():

    distance = float(input("digite a distancia da viagem: "))
    valor_inicial = float(input("digite o valor inicial do taximetro: "))
    taxa_var = float(input("digite a taxa variavel: "))
    print(f"valor da viagem: {taximetro(distance, valor_inicial, taxa_var)}")
if __name__ == '__main__': 
    main()