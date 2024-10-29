import re

def extrair_palavras(texto):
    padrao = re.compile(r'\b\w+\b')
    palavras = padrao.findall(texto)
    return palavras

def main():
    texto = "Beleza! Este é um ótimo exemplo, você não acha?"
    lista_palavras = extrair_palavras(texto)
    print(lista_palavras)

if __name__ == "__main__":
    main()