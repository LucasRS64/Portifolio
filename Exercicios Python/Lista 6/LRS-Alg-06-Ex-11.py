import random

def gerar_bilhete_mega_sena():
    numeros = random.sample(range(1, 61), 6)  
    numeros.sort()  
    return numeros

def main():
    bilhete = gerar_bilhete_mega_sena()
    print("Seu bilhete da Mega-Sena é:")
    print(bilhete)

if __name__ == "__main__":
    main()