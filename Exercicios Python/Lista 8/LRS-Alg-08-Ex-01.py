def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def main():
    test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in test_values:
        print(f"{value}! = {fatorial(value)}")

if __name__ == "__main__":
    main()