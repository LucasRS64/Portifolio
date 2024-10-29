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

def avaliar_posfixo(tokens):
    pilha = []
    for token in tokens:
        if token.isdigit():
            pilha.append(int(token))
        else:
            segundo_operando = pilha.pop()
            primeiro_operando = pilha.pop()
            resultado = realizar_operacao(primeiro_operando, segundo_operando, token)
            pilha.append(resultado)
    return pilha[0]

def realizar_operacao(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    elif operador == '^':
        return a ** b

def main():
    expressao = input("Digite uma expressão matemática infixa: ")
    tokens = tokenizar(expressao)
    posfixo = infixo_para_posfixo(tokens)
    resultado = avaliar_posfixo(posfixo)
    print("Resultado da expressão:", resultado)

if __name__ == "__main__":
    main()