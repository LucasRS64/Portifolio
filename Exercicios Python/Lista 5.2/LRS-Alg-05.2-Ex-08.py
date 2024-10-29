def formatacao(frase) :
    frase_formatada = ''
    capitalize_prox = True
    for char in frase :
        if char == 1 :
            frase_formatada += char.upper()
        if char == '.' or char == '!' or char == '?' :
            capitalize_prox = True
        elif char != ' ' and capitalize_prox :
            frase_formatada += char.upper()
            capitalize_prox = False
            continue
        frase_formatada += char

    return frase_formatada

           

    
def main():
   frase = input("digite a frase a ser formatada: ")
   print(formatacao(frase))
if __name__ == '__main__': 
    main()