import string

def sao_anagramas_frases(frase1, frase2):
    frase1 = ''.join(char for char in frase1 if char not in string.punctuation + " ").lower()
    frase2 = ''.join(char for char in frase2 if char not in string.punctuation + " ").lower()

    contador_frase1 = {}
    contador_frase2 = {}

    for char in frase1:
        if char in contador_frase1:
            contador_frase1[char] += 1
        else:
            contador_frase1[char] = 1

    for char in frase2:
        if char in contador_frase2:
            contador_frase2[char] += 1
        else:
            contador_frase2[char] = 1

    return contador_frase1 == contador_frase2

# Teste da função
print(sao_anagramas_frases("William Shakespeare", "I am a weakish speller"))  
print(sao_anagramas_frases("Hello world", "World hello"))  
print(sao_anagramas_frases("Hello", "World"))  