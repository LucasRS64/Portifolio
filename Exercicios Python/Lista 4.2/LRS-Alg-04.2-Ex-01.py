soma_media = 0
total_numeros = 0
while True:
    x = float(input("digite um numero para a media ou 0 para finalizar: "))
    soma_media += x
    if (soma_media == 0) :
        print("ERRO: o primeiro valor nao pode ser 0")
        break
    if x == 0:
        break   
    total_numeros += 1
media_final = soma_media / total_numeros
print(f'a media é {media_final}')