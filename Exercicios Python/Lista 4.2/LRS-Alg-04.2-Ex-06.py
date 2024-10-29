sentenca = ""
verificador = 0

while True :
    r = input("Digite um bit para descobir a paridade: ")
    if r == "":
        break
    if (r == 0 or r == 1) :
        sentenca = sentenca + r
        verificador += 1
    else :
        print("Erro: nao condiz com uma sequencia de bits")

element_key = "1"
sentenca.count(element_key)

if (verificador > 8) :
    print("Erro: nao e uma sequencia de 8 bits.")
if (sentenca.count(element_key) % 2 == 0) :
    print("paridade par")
if (sentenca.count(element_key) % 2 != 0) :
    print("paridade impar")
print(sentenca)
