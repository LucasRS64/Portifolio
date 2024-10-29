#Escreva um programa Python que peça para o usuário uma letra do
#alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
#mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
#mensagem informando que a letra é uma consoante.

x = str(input("coloque a letra: "))

x1 = x.upper()

if (x1 !='A' and x1 != 'E' and x1 != 'I' and x1 != 'O' and x1 != 'U') :
    print("Cosoante")
else :
    print("Vogal")