def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in test_values:
        print(f"Fibonacci({value}) = {fibonacci(value)}")

if __name__ == "__main__":
    main()