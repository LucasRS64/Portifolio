def primo(num) :
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    
 num = int(input("digite um numero para verificar se e primo: "))
 if (primo(num)) :
    print("o numero e primo")
 else :
    print("nao e primo")
if __name__ == "__main__":
    main()