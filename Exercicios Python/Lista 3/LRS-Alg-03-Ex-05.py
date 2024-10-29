#A quantidade de dias de um m6es pode variar de 28 a 31
#dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de
#um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
#quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
#“28 ou 29 dias”.

mes = str(input("Qual o nome do mes? "))


if (mes == 'Fevereiro') :
    print("entre 28 a 29")
else :
    print("entre 28 a 31")
    