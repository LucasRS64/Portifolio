def tokenizar(expressao):
    tokens = []
    numero = ''
    for caractere in expressao:
        if caractere.isdigit() or (caractere == '-' and not numero):  
            numero += caractere
        else:
            if numero: 
                tokens.append(numero)
                numero = ''
            if caractere.strip():  
                tokens.append(caractere)
    if numero:  
        tokens.append(numero)
    return tokens

def main():
    expressao = input("Digite uma expressão matemática: ")
    tokens = tokenizar(expressao)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()