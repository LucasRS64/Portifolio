#Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
#usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
#exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
#Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
#deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
#quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
#usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.

brita = 130
cort_grama = 106
despt = 70
sala_sil = 40

x = int(input("digite o valor em Db: "))


if (x == brita) :
    print("Britadeira")
elif (x == cort_grama) :
    print("Cortador de Grama")
elif (x == despt) :
    print("Despertador")
elif (x == sala_sil) :
    print("Sala silenciosa")
elif (x < sala_sil) :
    print("menor que uma sala silenciosa")
elif (x > sala_sil and x < despt) :
    print("entre uma sala silenciosa e um despertador")
elif (x > despt and x < cort_grama) :
    print("entre um despertador e um cortador de grama")
elif (x > cort_grama and x < brita) :
    print("entre um cortador de grama e uma britadeira")
elif (x > brita) :
    print("Superior a uma britadeira")


