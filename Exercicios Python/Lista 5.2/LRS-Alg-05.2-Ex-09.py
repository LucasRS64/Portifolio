def isInteger(s):
    s = s.strip()

    if len(s) == 0:
        return False

    if s[0] in ['+', '-']:  
        s = s[1:]  

    return s.isdigit()

def main():
    entrada = input("Digite uma string para verificar se representa um número inteiro: ")
    if isInteger(entrada):
        print("A string representa um número inteiro.")
    else:
        print("A string não representa um número inteiro.")

if __name__ == "__main__":
    main()