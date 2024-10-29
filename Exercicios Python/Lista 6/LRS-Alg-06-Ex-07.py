def divisible_and_Perfect(n) :
    soma_divisores = 0
    for x in range(1, n) :
     if n % x == 0:
        soma_divisores += x
    return soma_divisores == n

def main():
    listaN = []
    for num in range(1, 10001):
     if divisible_and_Perfect(num) :
        listaN.append(num)
    print(listaN)    
    
if __name__ == "__main__":
    main()