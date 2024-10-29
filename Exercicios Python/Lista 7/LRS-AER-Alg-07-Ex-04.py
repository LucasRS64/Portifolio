def traduzir_para_morse(mensagem):
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    morse_mensagem = ""
    for char in mensagem:
        if char.upper() in morse:
            morse_mensagem += morse[char.upper()] + " "
    return morse_mensagem

def main():
    mensagem = input("Digite a mensagem para traduzir para código Morse: ")
    mensagem_traduzida = traduzir_para_morse(mensagem)
    print("Mensagem em código Morse:")
    print(mensagem_traduzida)

if __name__ == "__main__":
    main()