import random
def random_password() :
    
    comprimento = random.randint(7, 10)
    senha = ''.join(chr(random.randint(33, 126)) for _ in range(comprimento))
    return senha
def main():
    print(f"senha aleatoria gerada: {random_password()}")
if __name__ == "__main__":
    main()