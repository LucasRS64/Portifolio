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

def infixo_para_posfixo(tokens):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    posfixo = []
    operadores = []

    for token in tokens:
        if token.isdigit():
            posfixo.append(token)
        elif token in precedencia:
            while operadores and precedencia.get(operadores[-1], 0) >= precedencia[token]:
                posfixo.append(operadores.pop())
            operadores.append(token)
        elif token == '(':
            operadores.append(token)
        elif token == ')':
            while operadores and operadores[-1] != '(':
                posfixo.append(operadores.pop())
            operadores.pop()

    while operadores:
        posfixo.append(operadores.pop())

    return posfixo

def main():
    expressao = input("Digite uma expressão matemática infixa: ")
    tokens = tokenizar(expressao)
    posfixo = infixo_para_posfixo(tokens)
    print("Expressão pós-fixada:", ' '.join(posfixo))

if __name__ == "__main__":
    main()