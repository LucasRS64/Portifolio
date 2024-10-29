mensagem = str(input("Digite a mensagem: "))
deslocamento = int(input("Valor de deslocamento: "))
mensa_encryp = ''
for x in mensagem:
    if x.isalpha :
        if x.islower():
            mensa_encryp += chr((ord(x) - 97 + deslocamento) % 26 + 97)
        elif x.isupper() :
            mensa_encryp += chr((ord(x) - 65 + deslocamento) % 26 + 65)
    
print("Mensagem criptografada: ", mensa_encryp)
