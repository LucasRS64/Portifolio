string_original = input("digite a palavra para verificar se e palindromo: ")
correct = 0
string_original = string_original.lower()
palavra_invertida = string_original[::-1]
for x in range(0, len(string_original)) :
    if string_original[x] == palavra_invertida[x] :
        correct += 1
    else :
        print("Nao e palindromo")
        break

if (correct == len(string_original)) :
    print("A palavra e palindromo.")