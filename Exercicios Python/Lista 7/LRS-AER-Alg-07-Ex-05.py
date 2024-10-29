def sao_anagramas(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    contador_str1 = {}
    contador_str2 = {}

    for char in str1:
        if char in contador_str1:
            contador_str1[char] += 1
        else:
            contador_str1[char] = 1

    for char in str2:
        if char in contador_str2:
            contador_str2[char] += 1
        else:
            contador_str2[char] = 1
    return contador_str1 == contador_str2

print(sao_anagramas("amor", "roma"))  
print(sao_anagramas("Hello", "World"))  